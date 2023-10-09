Feature: bulk actions performing in opportunity list page
  @opportunity
  Scenario: In bulk actions adding label
    When select four opportunities in opportunity list
    And click in Add _label
    And select label and click on savee
    Then validate label is added or nott

  @opportunity
  Scenario: assigning Opportunity owner by bulk
    When select four opportunities in opportunity list
    And click on Assigned Opportunity owner button
    And select assigned opportunity leader and click save
    Then validate assigned opportunity leader is changed or not


#
#
#  Scenario: sending mail in bulk actions
#    When select two leads in opportunity list
#    And click on send _email
#    And select _sender
#    And write subject line of mail _as "payment need to pay"
#    And check tab pop is working or not in to _area
#    And select _placeholders
#    And attach any documnet and validate document added or _not
#    And now click _delete
#    And check delete alert pop up is opened or not and click no on delete _alert
#    And now send mail button _click
#    Then check on messages wheather the mail is send or not and click opportunity