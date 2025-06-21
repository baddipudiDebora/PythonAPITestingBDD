# Created by Debora at 6/21/2025
Feature: DELETE User


  Scenario: 01 DELETE User valid flow
    Given I call the "DELETE" verb request for the endpoint "DELETEUser"
    And I add the path params
      | key      | value |
      | username | DebX  |
    When I attach headers
    When I send the request
    Then I validate the status code is '200'