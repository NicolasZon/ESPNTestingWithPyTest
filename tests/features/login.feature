@login
Feature: Create an ESPN account
  As a sport lover, I want to log into my ESPN account

Background:
    Given the ESPN page is displayed

  Scenario: Log into ESPN web page
    When the user performs the flow to log into ESPN
    Then the user can see her name in the user section