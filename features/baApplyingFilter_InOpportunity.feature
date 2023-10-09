Feature: Applying filter and create tab and check in kanban view
  @opportunity
  Scenario: check it is in open or not
    When click on opportunity
    Then check in opportunity page that it automatically in openfilter
  @opportunity
  Scenario Outline: create filter Tab in opportunity page
    When click on All opportunities filter button
    When click on filter _button
    And select _attributes you want to filter "<source>" and "<type>" andtabName "<name>"
    And click _create button
    And validate tab is created or _nott
    And click on kanban view and check it is selected in created filter or not "<name>"
    And back to list view
    When click on new filter tab and _deltee
    And now check tab is deleted or _nott
    Then check in opportunity page that it automatically in openfilter

    Examples:
    |source     |     type  | name            |
    |Sub        | Face      |  facebook       |
    |Source     | Digi      |  All digital    |
    |Assign     | Venk      |  Assigne      |