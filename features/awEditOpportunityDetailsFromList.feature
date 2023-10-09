Feature: changing stage ,label,opportunity owner from opportunity list
  @opportunity
  Scenario: changing stage from opportunity list
    When click on Opportunity link to go back
    And go on stage coloumn and change stage option
    Then validate in Activity area wheather stage is changed or not

  @opportunity
  Scenario: changing labels selecting non selected labels and deselecting selected labels in opportunity list
    When click on Opportunity link to go back
    And go on labels column and change labels in opportunity list
    Then validate in Activity area wheather labels are changed or _not
  @opportunity
  Scenario: change Opportunity owner
    When click on Opportunity link to go back
    Then go on opportunity owner coloumn change lead owner and Validatee