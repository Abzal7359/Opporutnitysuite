Feature: Adding site visit on opportunity profile
  @opportunity
  Scenario: Add site visit of feature in opportunity profile
    When click on site _Visits
    And click on Add site visit _option
    And fill site visit _details
    |date        |time   |
    |30-11-2023  |  1130     |
    And click save _button
    Then check site visit is added or _not
  @opportunity
  Scenario: Add site visit of past in opportunity profile
    When click on Add site _visitoption
    And fill site visit past _details
    |date        |time   |
    |05-08-2023  |  1630     |
    Then check site visit is added or _not