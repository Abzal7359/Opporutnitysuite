Feature: Export functionality for report generation in opportunity
  @opportunity
  Scenario: Export report with some choose columns in opportunity columns
    When click on _Export
    And now select which columns you need in _report
    And click on export _button
    And now go to downloads _section
    Then here validate report generated or _not