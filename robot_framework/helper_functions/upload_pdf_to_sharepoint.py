""" Script to upload fetch an OS2-formular submission and upload it in pdf format to Sharepoint. """
from urllib.parse import unquote, urlparse

import requests

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection

from mbu_dev_shared_components.msoffice365.sharepoint_api.files import Sharepoint


def upload_pdf_to_sharepoint(
    orchestrator_connection: OrchestratorConnection,
    sharepoint_api: Sharepoint,
    folder_name: str,
    os2_api_key: str,
    active_forms: list,
) -> None:
    """Main function to upload a PDF to Sharepoint."""

    orchestrator_connection.log_trace("Upload PDF to Sharepoint started.")
    print("Upload PDF to Sharepoint started.")

    existing_pdfs_sum = 0

    existing_pdfs = sharepoint_api.fetch_files_list(folder_name=folder_name)

    if existing_pdfs:
        existing_pdf_names = {file["Name"] for file in existing_pdfs}

    else:
        existing_pdf_names = set()

    for form in active_forms:
        file_url = form["data"]["attachments"]["besvarelse_i_pdf_format"]["url"]

        path = urlparse(file_url).path
        filename = path.split('/')[-1]
        final_filename = f"{unquote(filename)}"

        print(file_url)
        print(final_filename)

        if final_filename in existing_pdf_names:
            print(f"File {final_filename} already exists in Sharepoint. Skipping download.")

            existing_pdfs_sum += 1

            continue

        orchestrator_connection.log_trace("Downloading PDF from OS2Forms API.")
        print("Downloading PDF from OS2Forms API.")
        try:
            downloaded_file = download_file_bytes(file_url, os2_api_key)

        except requests.RequestException as error:
            orchestrator_connection.log_trace(f"Failed to download file: {error}")
            print(f"Failed to download file: {error}")

        # Upload the file to Sharepoint
        sharepoint_api.upload_file_from_bytes(
            binary_content=downloaded_file,
            file_name=final_filename,
            folder_name=folder_name
        )

    if existing_pdfs_sum == len(active_forms):
        orchestrator_connection.log_trace("All files already exist in Sharepoint. No new files uploaded.")
        print("All files already exist in Sharepoint. No new files uploaded.")


def download_file_bytes(url: str, os2_api_key: str) -> bytes:
    """Downloads the content of a file from a specified URL, appending an API key to the URL for authorization.
    The API key is retrieved from an environment variable 'OS2ApiKey'.

    Parameters:
    url (str): The URL from which the file will be downloaded.
    os2_api_key (str): The API-key for OS2Forms api.

    Returns:
    bytes: The content of the file as a byte stream.

    Raises:
    requests.RequestException: If the HTTP request fails for any reason.
    """

    headers = {
        'Content-Type': 'application/json',
        'api-key': f'{os2_api_key}'
    }

    response = requests.request(method='GET', url=url, headers=headers, timeout=60)

    response.raise_for_status()

    return response.content
