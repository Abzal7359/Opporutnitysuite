import re
import time

import webcolors
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.AddOpportunityDirectlyPage import AddOpportunityDirectlyPage
from pages.ApplyingFilter_InOpportunityPage import ApplyinFilter_InOpportunityPage
from pages.ApplyingFilter_createTabPage import ApplyingFilterCreateTab

import configparser

config = configparser.ConfigParser()
config.read(r'config.txt')


@when(u'click on opportunity')
def step_impl(context):
    context.AOD = AddOpportunityDirectlyPage(context.driver)
    context.AOD.click_opportunities_linkk()



@then(u'check in opportunity page that it automatically in openfilter')
def step_impl(context):
    context.AF=ApplyinFilter_InOpportunityPage(context.driver)
    assert context.AF.isDefault_in_openFilter()



@when(u'click on All opportunities filter button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//h6[normalize-space()='All Opportunities']").click()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))


@when(u'click on filter _button')
def step_impl(context):
    context.AF = ApplyinFilter_InOpportunityPage(context.driver)
    context.AF.click_add_filters_button()


@when(u'select _attributes you want to filter "{source}" and "{type}" andtabName "{name}"')
def step_impl(context,source,type,name):
    context.AFCT = ApplyingFilterCreateTab(context.driver)
    context.AFCT.select_filter_type(source, type)
    context.AFCT.click_create_tab()
    context.AFCT.enter_tab_name(name)

@when(u'click _create button')
def step_impl(context):
    context.AFCT.click_create_button()

@when(u'validate tab is created or _nott')
def step_impl(context):
    assert context.AFCT.is_TAB_Createdd_in_opportunity()



@when(u'click on kanban view and check it is selected in created filter or not "{name}"')
def step_impl(context,name):
    #(//*[name()='svg'][@class='w-6 h-6'])[3] for demo
    #(//*[name()='svg'][@class='w-6 h-6'])[2] for production
    context.driver.find_element(By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[2]//*[local-name()='svg']").click()
    time.sleep(5)
    ss = context.driver.find_element(By.XPATH, "//*[@id='opportunity-filters']/div/div[2]/div[2]/div/h6").text
    c = context.driver.find_element(By.XPATH,
                                    "//*[@id='opportunity-filters']/div/div[2]/div[2]/div").value_of_css_property(
        "background-color")

    match = re.match(r"rgba\((\d+), (\d+), (\d+), (\d+(\.\d+)?)\)", c)
    if match:
        r, g, b, a = map(int, match.group(1, 2, 3, 4))

        # Find the nearest color name for the RGB values
        color_name = webcolors.rgb_to_name((r, g, b))

        if color_name == "black" and ss == name:
            assert True
        else:
            assert False


@when(u'back to list view')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[1]//*[local-name()='svg']")))
    element.click()


    time.sleep(float(config.get('waiting_time', 'max_wait')))

@when(u'click on new filter tab and _deltee')
def step_impl(context):
    context.AFCT = ApplyingFilterCreateTab(context.driver)
    context.AFCT.click_delete_filterr_in_opportunity()

@when(u'now check tab is deleted or _nott')
def step_impl(context):
    zl = context.driver.find_elements(By.XPATH,"//div[@class='flex items-center cursor-pointer whitespace-nowrap']")
    if len(zl) == 4:
        return True
    else:
        return False





