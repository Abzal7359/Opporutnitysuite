import configparser
import time

from behave import *
from selenium.webdriver.common.by import By

from pages.AddSiteVisitPage import AddSiteVisitPage
config = configparser.ConfigParser()
config.read(r'config.txt')

@when(u'click on site _Visits')
def step_impl(context):
    context.ASVP=AddSiteVisitPage(context.driver)
    context.ASVP.clickOnSiteVisits_bar()



@when(u'click on Add site visit _option')
def step_impl(context):
    context.ASVP.createSite_Visit()


@when(u'fill site visit _details')
def step_impl(context):
    for row in context.table:
        context.ASVP.fill_siteVisit_details_opportunity(row["date"],row["time"])

@when(u'click save _button')
def step_impl(context):
    context.ASVP.click_On_Save()


@then(u'check site visit is added or _not')
def step_impl(context):
    assert context.ASVP.is_siteVisitAdded()


#past site visit
@when(u'click on Add site _visitoption')
def step_impl(context):
    context.ASVP = AddSiteVisitPage(context.driver)
    context.ASVP.createSite_Visit()


@when(u'fill site visit past _details')
def step_impl(context):
    for row in context.table:
        context.ASVP.fill_siteVisit_details_opportunity(row["date"], row["time"])
        context.driver.find_element(By.XPATH,"(//textarea[@id='notes'])[1]").send_keys("so much interested")
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        context.ASVP.click_On_Save()