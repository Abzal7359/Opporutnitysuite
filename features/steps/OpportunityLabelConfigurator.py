from behave import *
from selenium.webdriver.common.by import By
import time
from pages.LeadLabelsConfiguratorPage import LeadLabelsConfiguratorPage



@when(u'click settings gear imagee')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img").click()
    time.sleep(3)

@when(u'click on Opportunity button in label configurators')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.click_opportunity_button()

@when(u'click on add _label')
def step_impl(context):

    context.LLC.click_add_label()

@when(u'enter name of _label')
def step_impl(context):
    context.LLC.enter_label_name()

@when(u'validate label added or not in same _page')
def step_impl(context):
    assert context.LLC.validate_label_added()




@when(u'click on opportunity list')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.navigate_to_opportunity_list()


@then(u'check here in opportunity list that label is added or not')
def step_impl(context):
    assert context.LLC.check_label_in_opportunity_list()


@when(u'go to leads label configurator click opportunity button')
def step_impl(context):

    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.go_to_leads_label_configurator()
    context.driver.find_element(By.XPATH, "//*[@id='sub-menu-5']/span[2]/span/a").click()

@when(u'change position of _label')
def step_impl(context):
    context.LLC.change_label_position()


@then(u'check in opportuntiy list that label position is change or not')
def step_impl(context):
    assert context.LLC.check_label_position_in_Opportunity()


@when(u'delete the added _label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.delete_added_label()


@then(u'validate here onlly by seeing count of lead _labels')
def step_impl(context):
    assert context.LLC.validate_label_deletion()

@when(u'click on disable _button')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.disable_label()


@then(u'check in opportunity list the label is disabled or not')
def step_impl(context):
    assert context.LLC.check_label_disabled_in_opportunity()


@when(u'enable the _label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.enable_label()


@then(u'check in opportunity list labels wheather the able is enabled or not')
def step_impl(context):
    assert context.LLC.check_label_enabled_in_opportunity()


@when(u'change colour of one _label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.change_colour_label()

@then(u'validate colour is changed or _not')
def step_impl(context):
    assert context.LLC.is_Colour_Applied_in_opportunity()