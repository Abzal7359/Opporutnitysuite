Feature: edit profile in opportunity profile
  @opportunity
  Scenario: editing interest part of opportunity profile
    When click on _profile
    And click on edit _profile
    And go to interest area and edit details
    And click on save the button_
    Then check in opportunity section the updates reflected or not