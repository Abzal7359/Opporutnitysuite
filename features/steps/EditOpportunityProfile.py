from behave import *
from selenium.webdriver.common.by import By

from pages.LeadsProfile import LeadsProfile


@when(u'click on _activiy')
def step_impl(context):
    op = context.driver.find_element(By.XPATH, "(// a[normalize-space() = 'Activity'])[1]")
    context.driver.execute_script("arguments[0].click()", op)



@when(u'change _assignedPerson')
def step_impl(context):
    context.LDP = LeadsProfile(context.driver)
    context.LDP.clickToChangeAssignedPersonOfOpportunity()

@when(u'Change _label')
def step_impl(context):
    context.LDP.clickTo_Add_label_opportunity()


@when(u'change source type and _source')
def step_impl(context):
    context.LDP.clickTo_Change_source_Opportunity()


@when(u'change _campaign')
def step_impl(context):
    context.LDP.clickToChange_CampaignType_Opportunity()

@then(u'verify All Changed or _Not')
def step_impl(context):
    assert context.LDP.isLeadProfile_Modified_Opportunity()



