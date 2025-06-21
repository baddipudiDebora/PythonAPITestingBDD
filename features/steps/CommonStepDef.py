import json
import os

from behave import given, when, then
import api_utils  # Utility module for requests and config
import api_validations
from file_util import load_json_payload


@given('I call the "{api_verb}" verb request for the endpoint "{endpointname}"')
def step_impl(context, api_verb, endpointname):
    api_utils.setup_context_for_endpoint(context, api_verb,endpointname)


@given('I setup the query parameters "{query_params}"')
def step_impl(context,query_params):
    context.url = f"{context.base_url}?{query_params}"  # Append query parameters
    assert "/" in context.url , "Expected '/' means path params concatenated in the string"


@given("I add the path params '{pet_id}'")
def step_impl(context, pet_id):
    context.url = context.base_url.replace("{pet_id}", str(pet_id)) # Append query parameters
    print(context.url)

@given("I add the path params")
def step_impl(context):
    for row in context.table:
        placeholder = row['key']
        replacement = str(row['value'])
        context.url = context.url.replace(f"{{{placeholder}}}", replacement)


@given("I add a payload from '{jsonfileName}' json file")
def step_impl(context, jsonfileName):
    context.json_data = load_json_payload(jsonfileName)



@given("I load the payload from '{jsonfileName}' and override fields")
def step_impl(context, jsonfileName):
    context.json_data = api_utils.load_and_override_json(jsonfileName, context.table)


@when("I attach headers")
def step_attach_headers(context):
    """Headers are attached automatically by utility functions, but additional modifications can be done here."""
    context.headers = api_utils.get_headers(context)


@when("I send the request")
def step_send_request(context):
    api_utils.log_request_context(context)
    api_utils.send_request_for_context(context)


@then("I validate the status code is '{expected_status}'")
def step_validate_status(context, expected_status):
    api_validations.assert_status_code(context.response, expected_status)

