Feature: creating opportunity stages under ->Data management and adding automations and validating
  @opportunity @t
  Scenario:creating opportunity stage and validating created or not
    When click on opportunity stages under Data mangement
    And fill details of stage like stage name
    And set colours of stage
    Then validate stage created or not in opportunity list also
  @opportunity @t
  Scenario: Drag and drop of stage and validate
    When back to setting and in opportunity stages
    When drag and drop created stage at one step less
    Then validate the stage position is changed or not in opportunity list also
  @opportunity @t
  Scenario:disable the stage and validate it
    When back to setting and in opportunity stages
    And click disable buttoon
    Then validate disabled or not
  @opportunity @t
  Scenario:creating automation task and automation stage conversion and validate
    When click on Add automation
    And create automation task
    And validate task automation created or not
    And create automation of stage changing
    Then validate automation stage created or not
  @opportunity @t
  Scenario: delete the stage and validate
    When click on delete the stage
    Then validate created stage deleted or not


