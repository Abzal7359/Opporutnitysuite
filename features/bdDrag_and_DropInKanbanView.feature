Feature: we test drag and drop in kanban view
  @opportunity
  Scenario: drag and drop one opportunity and check wheather it is in top and in activty area check
    When get text of stage
    When drag and drop from one stage
    And validate it is dropped or not
  @opportunity
  Scenario: drag and drop to won status
    When click back to kanban _view
    And select one element drag and drop into won status
    And check it is dropped or not

  @opportunity
  Scenario: drag and drop to lost status
    When click back to kanban _view
    And select one element drag and drop into lost status
    And enter lost reason and click save
    Then check it dropped into lost or not