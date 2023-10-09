Feature: checking Tasks section functionalities

  @opportunity @skip  @t
  Scenario: back to dashboard click settings back buttonn
    When click on setting link to go dashboard

  @opportunity @t
  Scenario: creating task tomorrow date and validating time and date for opportunities
    When go on opportunities
    And click one lead
    And create task and get date and time
    And got TASKS section
    And apply filters like assigne and date
    Then check the task is showing or not
  @opportunity @t
  Scenario:  change status from TASKS page and check in activity area for opportunity member
    When click on status change to completed
    And selecte completed filter and validate it is in completed filter or not
    Then click on that person and check in activity area Task update got or not

