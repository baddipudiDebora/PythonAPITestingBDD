from behave import given, when, then
import api_utils  # Utility module for requests and config

@given('I call the "{api_verb}" verb request for the endpoint "{endpoint_name}" with path parameters "{pet_id}"')
def step_impl(context, api_verb, endpoint_name, pet_id):
    """Stores the request details and sends API request"""
    context.api_verb = api_verb
    context.url = api_utils.get_url(endpoint_name, pet_id)
    print(context.url)


@given('I call the "{api_verb}" verb request for the endpoint "{endpoint_name}" with query parameters "{query_params}"')
def step_impl_query(context, api_verb, endpoint_name, query_params):
    context.api_verb = api_verb
    context.base_url = api_utils.get_url(endpoint_name)  # Get the base URL without pet_id
    context.url = f"{context.base_url}?{query_params}"  # Append query parameters
    assert "/" in context.url , "Expected '/' means path params concatenated in the string"
    print(context.url)

@when("I attach headers")
def step_attach_headers(context):
    """Headers are attached automatically by utility functions, but additional modifications can be done here."""
    context.headers = api_utils.get_headers()

@when("I send the request")
def step_send_request(context):
    context.response = api_utils.send_request(context.api_verb, context.url, context.headers)
    if not hasattr(context, "response"):
        raise RuntimeError("Response not found. Ensure the request step runs before this step.")

@then("I validate the status code is '{expected_status}'")
def step_validate_status(context, expected_status):
    """Validates the response status code"""
    actual_status = context.response.status_code
    assert str(actual_status) == expected_status, f"Expected {expected_status}, but got {actual_status}"
    print(f"Response Status: {actual_status}")


@given('I call the "{api_verb}" verb request for the endpoint "{endpointname}"')
def step_impl(context, api_verb, endpointname):
    context.api_verb = api_verb
    context.url = api_utils.get_url(endpointname)
    context.base_url = api_utils.get_url(endpointname)  # Get the base URL without pet_id


@given('I setup the query parameters "{query_params}"')
def step_impl(context,query_params):
    context.url = f"{context.base_url}?{query_params}"  # Append query parameters
    assert "/" in context.url , "Expected '/' means path params concatenated in the string"
    print(context.url)



@given("I add the path params '{pet_id}'")
def step_impl(context, pet_id):
    context.url = context.base_url.replace("{pet_id}", str(pet_id)) # Append query parameters
    print(context.url)