# Created by Debora at 6/19/2025
Feature: POST_pet. feature


  Scenario: Valid flow POST_pet
    Given I call the "GET" verb request for the endpoint "PETByID"
    Given I add the path params '5'
    When I attach headers
    When I send the request
    Then I validate the status code is '200'