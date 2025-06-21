# Created by Debora at 6/14/2025
Feature: Validate PET API Endpoints

  Scenario: Retrieve pet details by ID
    Given I call the "GET" verb request for the endpoint "PETByID"
    And I add the path params
      | key    | value |
      | pet_id | 1     |
    When I attach headers
    When I send the request
    Then I validate the status code is '200'





