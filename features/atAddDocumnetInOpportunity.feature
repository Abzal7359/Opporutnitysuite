Feature: Adding document in opportunity profile
  @opportunity
  Scenario: Document is uploading in document  section of opportunity profile
    When user clicks on Document _option
    And in that page he clicks Add _Documents
    And user upload file _here
    And clicks _save
    Then check wheather the file is uploaded or _not