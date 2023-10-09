Feature: checking in kanban view the count of tasks and notes showing correct
  @opportunity
  Scenario: In kanban view click on dropdown of opportunity and checking that It is showing details
    When click on kanban view button
    And click on dropdown of one opportunity and check it is showing details or not
    And get text of how many tasks and notes count
    And click on that oppportunity
    And create task and validate in activity area
    And create note and validate in activity area
    Then validate the task and note count is reflected or not in kanban view dropdown
