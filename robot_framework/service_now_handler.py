"""Test the ServiceNow API."""

import requests


PROD_INSTANCE = "aarhuskommune"
TEST_INSTANCE = "aarhuskommunedev"


def post_incident(orchestrator_connection, service_now_api_username, service_now_api_password, error_dict):
    """POST a CSM case by sys_id or case number."""

    print("inside post_incident() function ...")

    error_type = error_dict.get("type", "")  # Would typically be "ApplicationException"
    error_count = error_dict.get("error_count", "")  # The error_count
    error_message = error_dict.get("message", "")  # The actual Exception message in str format
    error_trace = error_dict.get("trace", "")  # The traceback.format_exc() in str format

    # post_url = f"https://{PROD_INSTANCE}.service-now.com/api/now/table/incident"
    post_url = f"https://{TEST_INSTANCE}.service-now.com/api/now/table/incident"

    incident_data = {
        "contact_type": "integration",  # Should always be 'integration' - this just means the incident was created using the ServiceNow API
        "short_description": f"Process name: {orchestrator_connection.process_name}, Error type: {error_type}",
        "description": f"Error count: {error_count}, Error message: {error_message}Full error trace message: {error_trace}",
        "business_service": "",  # What should this be?
        "service_offering": "",  # What should this be?
        "assignment_group": "b54156a91ba5115068ba5398624bcb0e",  # MBU Proces & Udvikling Assignment Group - should this be a constant in Orchestrator?
        "assigned_to": "",  # Should remain empty as placeholder for future assignment?

        "category": "Fejl",
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # pylint: disable=missing-timeout
    response = requests.post(post_url, json=incident_data, headers=headers, auth=(service_now_api_username, service_now_api_password))

    print()
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

    # pylint: disable=no-else-return
    if response.status_code == 200:
        return response.json().get("result", {})

    else:
        print(f"Error {response.status_code}: {response.text}")

        return None