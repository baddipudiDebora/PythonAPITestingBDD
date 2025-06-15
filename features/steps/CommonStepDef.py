from behave import *
import configparser
import json
import requests

use_step_matcher("re")


@given("I call the 'GET' verb request for the endpoint 'PETByID'")
def step_impl(context):
 url = "https://petstore.swagger.io/v2/pet/1"
 headers = {"Content-Type": "application/json"}
 response = requests.get(url, headers=headers)

 # Print response status and data
 print("Status Code:", response.status_code)
 print("Response JSON:", response.json())


@when("I attach headers")
def step_impl(context):
  pass


@when("I send the request")
def step_impl(context):
   pass


@then("I validate the status code is '200'")
def step_impl(context):
    pass