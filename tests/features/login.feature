@login
Feature: Create an ESPN account
  As a sport lover, I want to log into my ESPN account

  Background:
    Given the ESPN page is displayed

  Scenario Outline: Log into ESPN web page
    When the user performs the flow to log into ESPN with "<mail>" and "<password>"
    Then the user can see the "<name>" in the user section

    Examples:
    | name    | mail                  | password        |
    | Pedrito | pedritoperez@mail.com | pedritoperez123 |