import config
from behave import *
import configparser
import json
import requests
import json
from behave import use_step_matcher
import os
from Config import config

import requests

@given("I call the 'GET' verb request for the endpoint 'PETByID'")
def step_impl(context):
    url = config.get_url("PETByID", pet_id=1)  # Dynamic pet ID
    headers = config.get_headers()

    response = requests.get(url, headers=headers)
    print("Response:", response.json())



@when("I attach headers")
def step_impl(context):
  pass


@when("I send the request")
def step_impl(context):
   pass


@then("I validate the status code is '200'")
def step_impl(context):
    pass