Feature: performing bulk actions in kanban view
  @opportunity
  Scenario: changing labels in bulk action in kanban view
    When select four opportunities in kanban view
    And click on add label for bulk
    And select label from dropdown and save it
    Then valiadte that labels added by count and by checking in dropdown that all labels are showing
  @opportunity
  Scenario: changing Assigne opportunity owner in kanban view
    When select four opportunities in kanban view
    And click on Assign Opportunity Owner
    And select assigning person from dropdown and save it
    Then validate that assigne person is updated or not


