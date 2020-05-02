@signup
Feature: Delete an ESPN account
  As a sport lover, I want to delete my account in ESPN web page

  Background:
    Given there is data created previously
    And the ESPN page is displayed

  Scenario: Sign up with a new user in ESPN web page
    When the user performs the flow to delete his account
    Then the user can see her name in the user section