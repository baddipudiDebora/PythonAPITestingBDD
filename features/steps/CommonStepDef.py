import json
import os

from behave import given, when, then
import api_utils  # Utility module for requests and config
import api_validations
from file_util import load_json_payload


@given('I call the "{api_verb}" verb request for the endpoint "{endpointname}"')
def step_impl(context, api_verb, endpointname):
    context.api_verb = api_verb
    print(context.api_verb)
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


@given("I add a payload from '{jsonfileName}' json file")
def step_impl(context, jsonfileName):
    context.json_data = load_json_payload(jsonfileName)


@when("I attach headers")
def step_attach_headers(context):
    """Headers are attached automatically by utility functions, but additional modifications can be done here."""
    context.headers = api_utils.get_headers(context)


@when("I send the request")
def step_send_request(context):
    api_utils.log_request_context(context)

    if context.api_verb.upper() == "POST":
        context.response = api_utils.send_request(
            api_verb=context.api_verb,
            url=context.url,
            headers=context.headers,
            jsondata=context.json_data
        )
    else:
        context.response = api_utils.send_request(
            api_verb=context.api_verb,
            url=context.url,
            headers=context.headers
        )

    if not hasattr(context, "response"):
        raise RuntimeError("Response not found. Ensure the request step runs before this step.")

@then("I validate the status code is '{expected_status}'")
def step_validate_status(context, expected_status):
    api_validations.assert_status_code(context.response, expected_status)

