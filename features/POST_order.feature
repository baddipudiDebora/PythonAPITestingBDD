# Created by Debora at 6/20/2025
Feature:Place an order for a pet

  Scenario: Valid order placed for purchasing the pet
    Given I call the "POST" verb request for the endpoint "ORDER_PET"
    Given I add a payload from 'ORDER_PET' json file
    When I attach headers
    When I send the request
    Then I validate the status code is '200'