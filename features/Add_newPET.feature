# Created by Debora at 6/21/2025
Feature: POST_pet. feature

  Scenario: Valid flow Add new pet
    Given I call the "POST" verb request for the endpoint "CREATEUserList"
    Given I load the payload from 'AddNew_PET' and override fields
      | field       | value                                      |
      | name        | MrFluff                                    |
      | status      | available                                  |
      | tags.0.name | FluffyTag                                  |
      | photoUrls   | ["http://image1.com", "http://image2.com"] |
    When I attach headers
    When I send the request
    Then I validate the status code is '200'
