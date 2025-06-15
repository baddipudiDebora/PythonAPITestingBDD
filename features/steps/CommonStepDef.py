from behave import given, when, then
import api_utils  # Import the utility module

@given('I call the "{api_verb}" verb request for the endpoint "{endpoint_name}" with path parameters "{pet_id}"')
def step_impl(context, api_verb, endpoint_name, pet_id):
    """Stores the request details and sends API request"""
    url = api_utils.get_url(endpoint_name, pet_id)
    headers = api_utils.get_headers()
    print(url)
    context.response = api_utils.send_request(api_verb, url, headers)

@when("I attach headers")
def step_attach_headers(context):
    """Headers are attached automatically by utility functions, but additional modifications can be done here."""
    context.headers = api_utils.get_headers()

@when("I send the request")
def step_send_request(context):
    """Ensures request is sent within another step if needed"""
    if not hasattr(context, "response"):
        raise RuntimeError("Response not found. Ensure the request step runs before this step.")

@then("I validate the status code is '{expected_status}'")
def step_validate_status(context, expected_status):
    """Validates the response status code"""
    actual_status = context.response.status_code
    assert str(actual_status) == expected_status, f"Expected {expected_status}, but got {actual_status}"
    print(f"Response Status: {actual_status}")
