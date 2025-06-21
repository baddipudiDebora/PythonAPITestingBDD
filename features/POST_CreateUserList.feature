# Created by Debora at 6/21/2025
Feature:  Create user with createWithList

  Scenario: 001 valid flow Create user with createWithList
    Given I call the "POST" verb request for the endpoint "CREATEUserList"
    #Given I add a payload from 'AddNewUserList' json file
    Given I load the payload from 'AddNewUserList' and override fields
      | field      | value |
      | 0.username | DebX  |
      | 1.id       | 99    |
    When I attach headers
    When I send the request
    Then I validate the status code is '200'