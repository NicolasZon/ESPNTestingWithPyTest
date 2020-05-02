@signup
Feature: Create an ESPN account
  As a sport lover, I want to have my own account in ESPN web page

  Background:
    Given the ESPN page is displayed

  Scenario: Sign up with a new user in ESPN web page
    When the user performs the flow to create a new account
    Then the user can see her name in the user section