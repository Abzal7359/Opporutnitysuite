from behave import *
from selenium.webdriver.common.by import By

from pages.LeadsPage import LeadsPage

from pages.OpportunitiesPage import OpportunitiesPage


@when(u'select four opportunities in opportunity list')
def step_impl(context):
    # ------------------------------------
    context.LP =LeadsPage(context.driver)
    context.LP.selectFourLeadss()

@when(u'click in Add _label')
def step_impl(context):
    context.LP.click_add_label_button()


@when(u'select label and click on savee')
def step_impl(context):
    context.LP.select_label_item()


@then(u'validate label is added or nott')
def step_impl(context):
    assert context.LP.is_labels_selectedd()

#code to change Opportunity owner in bulk actions




@when(u'click on Assigned Opportunity owner button')
def step_impl(context):
    context.OP=OpportunitiesPage(context.driver)
    context.OP.click_assign_opportunity_owner_button()


@when(u'select assigned opportunity leader and click save')
def step_impl(context):
    context.OP.select_opportunity_owner()


@then(u'validate assigned opportunity leader is changed or not')
def step_impl(context):
    assert context.OP.isAssignedOpportunityOwner_Changed()

# code to send bulk  mail to opportunities
#-------------------------------------------------------------------
#
# @when(u'select two leads in opportunity list')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.select_two_leads()
#
#
# @when(u'click on send _email')
# def step_impl(context):
#     context.LP.click_send_email_button()
#
#
# @when(u'select _sender')
# def step_impl(context):
#     context.LP.select_sender()
#
#
# @when(u'write subject line of mail _as "{subject}"')
# def step_impl(context,subject):
#     context.LP.enter_subject(subject)
#
#
#
# @when(u'check tab pop is working or not in to _area')
# def step_impl(context):
#     assert context.LP.is_popUp_displayed()
#
#
#
# @when(u'select _placeholders')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.select_placeholders()
#
#
# @when(u'attach any documnet and validate document added or _not')
# def step_impl(context):
#     context.LP.attach_document("C://Users/abzalhussain/Desktop/download.jpeg")
#
#     assert context.LP.is_document_added()
#
#
#
# @when(u'now click _delete')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.click_delete_button()
#
#
# @when(u'check delete alert pop up is opened or not and click no on delete _alert')
# def step_impl(context):
#     assert  context.LP.is_delete_alert_displayed()
#
#
# @when(u'now send mail button _click')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.click_send_button()
#
#
#
# @Then(u'check on messages wheather the mail is send or not and click opportunity')
# def step_impl(context):
#     z=context.LP.check_mail_isSent_or_not()
#     context.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunities'])[1]").click()
#     assert z
