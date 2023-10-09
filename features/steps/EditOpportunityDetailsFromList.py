import time

from behave import *
from selenium.webdriver.common.by import By

from pages.EditOpportunityDetailsFromListPage import EditOpportunityDetailsFromListPage


# from pages import EditOpportunityDetailsFromListPage


@when(u'click on Opportunity link to go back')
def step_impl(context):
    context.EOPD=EditOpportunityDetailsFromListPage(context.driver)
    context.EOPD.click_opportunity_link()


@when(u'go on stage coloumn and change stage option')
def step_impl(context):
    # pass
    #in production below step is not usefull in uat stage is implemented
    context.EOPD.select_stage_option()




@Then(u'validate in Activity area wheather stage is changed or not')
def step_impl(context):
    # below two lines not neede  if stage implememted
    # context.driver.find_element(By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]").click()
    # time.sleep(3)
    assert context.EOPD.is_stage_change()




#changing labels from opportunity list
@when(u'go on labels column and change labels in opportunity list')
def step_impl(context):

    #------------------------------------------
    context.EOPD = EditOpportunityDetailsFromListPage(context.driver)
    context.EOPD.change_labels()


@Then(u'validate in Activity area wheather labels are changed or _not')
def step_impl(context):
    assert context.EOPD.validate_activity_area_labels_changed()




#change opportunity owner

@Then(u'go on opportunity owner coloumn change lead owner and Validatee')
def step_impl(context):
    context.EOPD = EditOpportunityDetailsFromListPage(context.driver)
    assert context.EOPD.change_opportunity_owner_and_validate()

