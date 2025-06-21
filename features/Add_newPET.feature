# Created by Debora at 6/21/2025
Feature: POST_pet. feature

  Scenario: Valid flow Add new pet
    Given I call the "POST" verb request for the endpoint "AddPet"
    Given I add a payload from 'AddNew_PET' json file
    When I attach headers
    When I send the request
    Then I validate the status code is '200'