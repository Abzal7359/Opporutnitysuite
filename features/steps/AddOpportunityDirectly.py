from behave import *
import time
from dataproviders import data
from pages.AddOpportunityDirectlyPage import AddOpportunityDirectlyPage
from selenium.webdriver import ActionChains
from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By

@when(u'enter login details and go to opportunities')
def step_impl(context):
    context.LOP = LoginPage(context.driver)
    context.LOP.enter_mail_and_password("masud.abdullah@bentolabs.io","Propflo@1234")
    context.LOP.clickSignIn()
    act = ActionChains(context.driver)
    (act
     .move_to_element(context.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))

     .move_to_element(context.driver.find_element(By.XPATH, "//a[normalize-space()='Leads']"))
     .click()
     .perform())
    time.sleep(3)


@when(u'click on opportunities link')
def step_impl(context):
    context.AOD = AddOpportunityDirectlyPage(context.driver)
    context.AOD.click_opportunities_link()


@when(u'click on Add opportunity button')
def step_impl(context):
    context.AOD.click_add_opportunity_button()


@when(u'enter full details')
def step_impl(context):
    for i in context.table:
        context.AOD.enter_opportunity_details(data.opportunity_phone, data.opportunity_name[0],
                                              data.opportunity_name[1], data.opportunity_mail)


@when(u'now click save button link')
def step_impl(context):
    context.AOD.click_to_save()


@then(u'check weather the opportunity is added or not')
def step_impl(context):
    assert context.AOD.is_opportunity_added()
