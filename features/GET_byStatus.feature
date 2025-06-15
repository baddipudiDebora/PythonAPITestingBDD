# Created by Debora at 6/15/2025
Feature: Validate PETstore GET by Status


  Scenario: 001 Retrieve pets using query parameters
    Given I call the "GET" verb request for the endpoint "FindByStatus" with query parameters "status=available"
    When I attach headers
    When I send the request
    Then I validate the status code is '200'

