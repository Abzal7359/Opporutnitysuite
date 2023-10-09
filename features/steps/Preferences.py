from behave import *
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@when(u'click on settings and click prefernces')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Preferences']").click()
    time.sleep(2)


@when(u'click on default kanban view button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Kanban view']").click()
    time.sleep(4)


@when(u'got to opportunities')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[contains(text(),'Settings')]").click()
    time.sleep(3)
    context.driver.refresh()
    time.sleep(5)
    act = ActionChains(context.driver)
    (act
     .move_to_element(context.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))

     .move_to_element(context.driver.find_element(By.XPATH, "//a[normalize-space()='Opportunities']"))
     .click()
     .perform())
    time.sleep(3)


@then(u'validate default view in kanban or not')
def step_impl(context):
    ele = context.driver.find_element(By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[2]")
    assert ele.get_attribute("class").__contains__("bg-[#DDE7EA] shadow-sm")


@when(u'click on default List view button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[@for='opportunityListView']").click()
    time.sleep(4)


@then(u'validate default view in List or not')
def step_impl(context):
    ele = context.driver.find_element(By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[1]")
    assert ele.get_attribute("class").__contains__("bg-[#DDE7EA] shadow-sm")


@when(u'collect any phone number')
def step_impl(context):
    global phn_number, person_name
    phn_number = context.driver.find_element(By.XPATH, "//tbody//td[3]").text.split()
    person_name = context.driver.find_element(By.XPATH, "//tbody//td[2]//div//div/following-sibling::span").text


@when(u'give input data in global search field')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@id='search-field']").send_keys(phn_number[1],Keys.ENTER)
    time.sleep(2)
@then(u'click the displayed person and validate we got same person or not')
def step_impl(context):
    context.driver.find_element(By.XPATH,f"//div[1]/div/div/div[1]/h6[contains(text(),'{person_name}')]").click()
    time.sleep(2)
    z=context.driver.find_element(By.XPATH,"//aside/div[2]/div[2]/div/div[2]/div[2]/span[2]").text
    assert z == phn_number[1]