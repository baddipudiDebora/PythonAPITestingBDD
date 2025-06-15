import config
from behave import *
import configparser
import json
import requests
import json

from behave import given
from Config import config  # Import the Config class


from behave import given
from Config import config


@when("I attach headers")
def step_impl(context):
  pass


@when("I send the request")
def step_impl(context):
   pass


@then("I validate the status code is '200'")
def step_impl(context):
    pass


@given('I call the "GET" verb request for the endpoint "PETByID" with pathparameters "{api_verb}", "{endpoint_name}", "{pet_id}"')
def step_impl(context, api_verb, endpoint_name, pet_id):
    print(f"API Verb: {api_verb}, Endpoint Name: {endpoint_name}, Pet ID: {pet_id}")

    print(f"Received API Verb: {api_verb}")
    print(f"Received Endpoint Name: {endpoint_name}")
    print(f"Received Pet ID: {pet_id}")


    url = config.get_url(endpoint_name, pet_id=pet_id)  # Dynamically fetch API URL
    headers = config.get_headers()

    if api_verb.lower() == "get":
        response = requests.get(url, headers=headers)
    elif api_verb.lower() == "post":
        response = requests.post(url, headers=headers)
    else:
        raise ValueError(f"Unsupported API verb: {api_verb}")

    print(f"Response for {api_verb} request to {endpoint_name} (Pet ID {pet_id}):", response.json())

