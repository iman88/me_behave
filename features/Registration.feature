@all
Feature: Verify registration functionality

  @sanity
  Scenario: Registration with valid data
    Given User is on Registration page
    When User enters username
    And User enters email id
    And User enters password
    And User clicks on signup button
    Then The user should be registered successfully

  @sanity @smoke
  Scenario: Registration with duplicate data
    Given User is on Registration page
    When User enters username
    And User enters email id
    And User enters password
    And User clicks on signup button
    Then The user should be registered successfully

  @abcd
  Scenario: Registration with duplicate username
    Given User is on Registration page
    When User enters username
    And User enters email id
    And User enters password
    And User clicks on signup button
    Then The user should be registered successfully