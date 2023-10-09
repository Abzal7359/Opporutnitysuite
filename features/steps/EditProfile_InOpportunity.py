import configparser
import time

from behave import *
from selenium.webdriver.common.by import By

from pages.Add_and_editProfilePage import AddAndEditProfilePage
config = configparser.ConfigParser()
config.read(r'config.txt')

@when(u'click on _profile')
def step_impl(context):
    #ADD edit profile page
    context.AEP=AddAndEditProfilePage(context.driver)
    context.AEP.clikcOnProfile()

@when(u'click on edit _profile')
def step_impl(context):
    context.AEP.clickOnEditProfile()

@when(u'go to interest area and edit details')
def step_impl(context):
    context.AEP.edit_interest_area_in_opportunityProfile()



@when(u'click on save the button_')
def step_impl(context):
    context.driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
    time.sleep(float(config.get('waiting_time', 'min_wait')))

@Then(u'check in opportunity section the updates reflected or not')
def step_impl(context):
    assert context.AEP.check_the_profile_isUpdated_inOpportunityArea()

