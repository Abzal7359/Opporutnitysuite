Feature: edit opportunity profile from left side
  @opportunity
  Scenario: edit opportunity profile from left side change all fields
    When click on _activiy
    When change _assignedPerson
    And Change _label
    And change source type and _source
    And change _campaign
    Then verify All Changed or _Not