@delete
Feature: Delete an ESPN account
  As a sport lover, I want to delete my account in ESPN web page

  Background:
    Given there is data created previously
    And the ESPN page is displayed

  Scenario: Delete user in ESPN web page
    When the user performs the flow to delete his account
    Then the user can see deleted account message