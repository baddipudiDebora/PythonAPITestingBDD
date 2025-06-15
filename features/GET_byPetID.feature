# Created by Debora at 6/14/2025
Feature: GET Pet By ID endpoint
  # Enter feature description here

  Scenario: 001 Status code 200 - Validate GET Pet By ID endpoint
    Given I call the "GET" verb request for the endpoint "PETByID" with pathparameters "GET", "PETByID", "1"
    When I attach headers
    When I send the request
    Then I validate the status code is '200'
