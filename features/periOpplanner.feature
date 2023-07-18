Feature: PeriOpPlanner

  Background:
    Given I am on the QA01 test site
    When I click the link for the PerOpPlanner
    Then I enter the userid and password
    And I click the login button

  Scenario Outline: Creating a new block
    Then I am on the periOpPlanner page
    And I click the menudropdown button
    And I select the block option
    And I click the create button
    And I select the Start Time as "<Start Time>"
    And I select the End Time as "<End Time>"
    And I select the Room as "<Room>"
    And I select the Block Group as "<Block Group>"
    And I click on the save button
    Then I am on the ReasonSelector screen
    And I select any reason
    And I click on the confirm button
    Examples:
      | Start Time |End Time|Room|Block Group|
      | 13:00      | 16:00  | OR3 | General Surgery  |





