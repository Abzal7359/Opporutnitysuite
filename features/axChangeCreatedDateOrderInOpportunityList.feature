Feature: change created Date order in Opportunity List page and check
  @opportunity
  Scenario: change created Date to descending order
    When clickon Opportunity button to back to opportunity
    And click on descending date _button
    Then validate dates in descending order or _not
  @opportunity
  Scenario: change created Date to Ascending order
    When click on ascending date _button
    Then validate dates in ascending order or _not
