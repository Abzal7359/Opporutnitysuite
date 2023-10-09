Feature: creating task for opportunity person
  @opportunity
  Scenario: Creating task in opportunity converted peerson
    When click on tasks _bar
    And click on create _task
    And write task and set task _details
    | textbox              | time       |
    | site visit tomorrow  | 1530       |
    And click task _save
    Then ckeck task is created or _not
  @opportunity
  Scenario:edit task like clone and adding comment
    When click on tasks _bar
    And click clone task and change priority and save
    And check task is cloned or not validate in activity area
    And click on view details on task and add comment
    Then check in activity area







    #//div[@class='flex flex-col']//div[1]//div[3]//p[1]
