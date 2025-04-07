"""This module contains the main process of the robot."""

import sys
import os
import json
import urllib.parse

from datetime import datetime

from io import BytesIO

import pandas as pd

import openpyxl

from sqlalchemy import create_engine

from openpyxl.styles import Alignment

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from itk_dev_shared_components.smtp import smtp_util

from mbu_dev_shared_components.msoffice365.sharepoint_api.files import Sharepoint

from robot_framework.helper_functions import formular_mappings

USERNAME = os.getenv("DADJ_EMAIL")
PASSWORD = os.getenv("DADJ_EMAIL_PASSWORD")
SHAREPOINT_FOLDER_URL = "https://aarhuskommune.sharepoint.com"
SHAREPOINT_SITE_NAME = "tea-teamsite10693"
SHAREPOINT_DOCUMENT_LIBRARY = "Delte dokumenter"

SHAREPOINT = Sharepoint(username=USERNAME, password=PASSWORD, site_url=SHAREPOINT_FOLDER_URL, site_name=SHAREPOINT_SITE_NAME, document_library=SHAREPOINT_DOCUMENT_LIBRARY)


# pylint: disable-next=unused-argument
def process(orchestrator_connection: OrchestratorConnection) -> None:
    """Do the primary process of the robot."""
    orchestrator_connection.log_trace("Running process.")

    sql_server_connection_string = orchestrator_connection.get_constant("DbConnectionString").value

    proc_args = json.loads(orchestrator_connection.process_arguments)

    os2_webform_id = proc_args["os2_webform_id"]

    excel_file_name = ""
    folder_name = ""

    if os2_webform_id == "sundung_aarhus":
        excel_file_name = "Dataudtræk SundUng Aarhus.xlsx"

        folder_name = "General/Udtræk OS2Forms"

    elif os2_webform_id == "henvisningsskema_til_klinisk_hyp":
        excel_file_name = "Henvisningsskema til klinisk hypnose.xlsx"

        folder_name = "General/Udtræk OS2Forms"

    # elif os2_webform_id == "en anden form":

    # STEP 1 - Get all active forms from the SQL server
    all_active_forms = get_forms_data(sql_server_connection_string, os2_webform_id)

    # STEP 2 - Get the Excel file from Sharepoint, if-logic to determine which file to fetch is needed
    excel_file = SHAREPOINT.fetch_file_using_open_binary(excel_file_name, folder_name)

    excel_stream = BytesIO(excel_file)

    excel_file_df = pd.read_excel(excel_stream)

    # Create a set of serial numbers from the Excel file
    serial_set = set(excel_file_df["Serial number"].tolist())

    # Initialize a list to store new forms
    new_forms = []

    # STEP 3 - Loop through all active forms and transform them to the correct format
    for form in all_active_forms:
        form_serial_number = form["entity"]["serial"][0]["value"]

        # if form_serial_number == 18:
        #     continue

        if form_serial_number in serial_set:
            continue

        transformed_row = formular_mappings.transform_form_submission(form_serial_number, form, formular_mappings.sundung_aarhus_mapping)

        new_forms.append(transformed_row)

        # print("form")
        # print(form)

        # print()
        # print()

        print("Transformed row:")
        print(transformed_row)

        print()
        print()

    # sys.exit()

    # STEP 4 - If new forms are found, append them to the Excel file and save it
    if new_forms:

        new_forms_df = pd.DataFrame(new_forms)

        # Append the new forms to the existing DataFrame
        updated_excel_df = pd.concat([excel_file_df, new_forms_df], ignore_index=True)

        # Sort by "Serial number" in descending order
        updated_excel_df.sort_values(by="Serial number", ascending=False, inplace=True)

        # Save the updated DataFrame to an in-memory Excel file
        updated_excel_stream = BytesIO()
        updated_excel_df.to_excel(updated_excel_stream, index=False, engine="openpyxl")
        updated_excel_stream.seek(0)

        # --- Start formatting ---
        # Load the workbook from the BytesIO stream
        wb = openpyxl.load_workbook(updated_excel_stream)
        ws = wb.active

        # Apply center alignment to all cells
        for row in ws.iter_rows():
            for cell in row:
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # Auto-adjust column widths based on content length
        for col in ws.columns:
            max_length = 0

            column_letter = col[0].column_letter  # Get column letter

            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))

            ws.column_dimensions[column_letter].width = max_length + 2

        # Save the formatted workbook back to a new BytesIO stream
        formatted_stream = BytesIO()
        wb.save(formatted_stream)
        formatted_stream.seek(0)
        # --- End formatting ---

        # Save the updated, formatted Excel file to SharePoint using helper function
        SHAREPOINT.upload_file_from_bytes(
            binary_content=formatted_stream.getvalue(),
            file_name=excel_file_name,
            folder_name=folder_name
        )

    else:
        print("No new forms found.")


def get_forms_data(conn_string: str, form_type: str) -> list[dict]:
    """
    Retrieve form_data['data'] for all matching submissions for the given form type.
    """

    print("inside get_forms_data")

    query = """
        SELECT
            form_id,
            form_data,
            CAST(form_submitted_date AS datetime) AS form_submitted_date
        FROM
            [RPA].[journalizing].[Forms]
        WHERE
            form_type = ?
        ORDER BY form_submitted_date DESC
    """

    # Create SQLAlchemy engine
    encoded_conn_str = urllib.parse.quote_plus(conn_string)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={encoded_conn_str}")

    try:
        # Run query with the form_type parameter as a list
        df = pd.read_sql(sql=query, con=engine, params=(form_type,))

        print("after pd.read_sql")

    except Exception as e:
        print("Error during pd.read_sql:", e)

        raise

    if df.empty:
        print("No submissions found for the given form type and date range.")

        return []

    # Extract the full parsed JSON for each row
    extracted_data = [
        json.loads(row["form_data"])
        for _, row in df.iterrows()
    ]

    return extracted_data


def send_excel_file(os2_webform_id: str, orchestrator_connection: OrchestratorConnection, filepath: str, start_date: datetime, end_date: datetime):
    """Function to send email with submissions list"""

    filename = filepath.split("\\")[-1]

    # Read excel file into BytesIO object
    wb = openpyxl.load_workbook(filepath)

    excel_buffer = BytesIO()

    wb.save(excel_buffer)

    excel_buffer.seek(0)

    proc_args = json.loads(orchestrator_connection.process_arguments)

    email_recipient = proc_args["email_recipient"]

    email_sender = orchestrator_connection.get_constant("e-mail_noreply").value

    email_subject = f"All submissions for {os2_webform_id} from {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}"

    email_body = proc_args["email_body"]

    attachments = [smtp_util.EmailAttachment(file=excel_buffer, file_name=filename)]

    smtp_util.send_email(
        receiver=email_recipient,
        sender=email_sender,
        subject=email_subject,
        body=email_body,
        smtp_server=orchestrator_connection.get_constant("smtp_server").value,
        smtp_port=int(orchestrator_connection.get_constant("smtp_port").value),
        html_body=True,
        attachments=attachments if attachments else None
    )
