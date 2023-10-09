Feature: Adding opportunity directly from opportunity lists dash board
  @opportunity @skip
  Scenario: login and going to opportunity
    When enter login details and go to opportunities

  @opportunity
  Scenario: adding opportunity from opportunity list
    When click on opportunities link
    And click on Add opportunity button
    And enter full details
    |mobile         |Fname      |Lname       |  email                    |
    |8978968428    | Manoj   |Kumar      |kumarmanoji1111@gmail.com     |
    And now click save button link
    Then check weather the opportunity is added or not



