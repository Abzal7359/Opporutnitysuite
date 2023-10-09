Feature: checking the opportunity view functionality working or not
  @opportunity @t
  Scenario: click Kanban view and validate the opportunities in default kanban or not
    When click on settings and click prefernces
    And click on default kanban view button
    And got to opportunities
    Then validate default view in kanban or not
  @opportunity @t
  Scenario: click in list view in preferences and validate
    When click on settings and click prefernces
    And click on default List view button
    And got to opportunities
    Then validate default view in List or not

    #//tbody//td[2]//div//div/following-sibling::span
  @opportunity @t
  Scenario: global search functionality
    When collect any phone number
    And give input data in global search field
    Then click the displayed person and validate we got same person or not






