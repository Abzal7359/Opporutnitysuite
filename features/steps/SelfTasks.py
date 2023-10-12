from behave import *
import time
from pages.DashboardPage import DashboardPage
from pages.TasksPage import TasksPage
from datetime import datetime, timedelta
from pages.LeadsPage import LeadsPage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


@when(u'click on setting link to go dashboard')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[contains(text(),'Settings')]").click()
    time.sleep(3)

@when(u'go to leads')
def step_impl(context):
    context.DP = DashboardPage(context.driver)
    context.DP = context.DP.clickOnLeads()


@when(u'click one lead')
def step_impl(context):
    global name
    name = context.driver.find_element(By.XPATH,
                                       "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[6]").text
    context.driver.find_element(By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[6]").click()
    time.sleep(3)


@when(u'create task and get date and time')
def step_impl(context):
    global assigne, date_time
    context.LP = LeadsPage(context.driver)
    context.TP = context.LP.clickOnTasksPage()
    time.sleep(2)
    context.TP.clickOnCreateTask()
    context.TP.enterTaskDetailss("hello", "1345")
    context.TP.clickOnTaskSave()
    assigne = context.driver.find_element(By.XPATH, "//app-task/div/div[3]/div/div/div[5]/div/p[3]/span/span[2]").text
    date_time = context.driver.find_element(By.XPATH, "//div[5]/div/p[4]/span/span[2]").text


@when(u'got TASKS section')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//span[contains(text(),'Tasks')])[1]").click()
    time.sleep(2)


@when(u'apply filters like assigne and date')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[2]/div/div[1]/div/div[4]/div/div/button[1]").click()
    time.sleep(1)
    labels = context.driver.find_elements(By.XPATH, "//app-select-dropdown/div/div/div/div")
    for i in labels:
        if i.text.lower() == assigne.lower():
            i.click()
            break

    time.sleep(2)

    context.driver.find_element(By.XPATH, "//div[2]/div/div[1]/div/div[3]/div/div/button[1]").click()
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Tomorrow']").click()
    time.sleep(3)


@then(u'check the task is showing or not')
def step_impl(context):
    # Get today's date
    today = datetime.now()

    # Calculate tomorrow's date
    tomorrow = today + timedelta(days=1)

    # Format tomorrow's date as "dd Mon yyyy"
    formatted_date = tomorrow.strftime("%d %b %Y")

    # Print the formatted date
    print(formatted_date)

    times = context.driver.find_elements(By.XPATH, "//tbody/tr/td[3]/div/div/p[1]")
    global row
    flag = True
    for j in range(1, len(times) + 1):

        d = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[3]/div/div/p[1]").text
        t = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[3]/div/div/p[2]").text
        v = context.driver.find_element(By.XPATH, f"//tbody//tr[{j}]//div/div[1]/div[2]/div[2]/div[1]/p").text
        if d in formatted_date and t in date_time and name == v:
            row = j
            flag = True
            break
        else:

            flag = False
    assert flag


@when(u'click on status change to completed')
def step_impl(context):
    context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]/div/div").click()
    context.driver.find_element(By.XPATH, "//label[text()='Completed ']").click()
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']").click()
    time.sleep(2)


@when(u'selecte completed filter and validate it is in completed filter or not')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@id='menu-button']").click()
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Completed']").click()
    time.sleep(3)


@then(u'click on that person and check in activity area Task update got or not')
def step_impl(context):
    many = context.driver.find_elements(By.XPATH, "//tbody/tr/td[3]/div/div/p[1]")
    flag = True
    for k in range(1, len(many) + 1):

        v = context.driver.find_element(By.XPATH, f"//tbody//tr[{k}]//div/div[1]/div[2]/div[2]/div[1]/p").text
        if name == v:

            print("completed task and in filter also")
            context.driver.find_element(By.XPATH, f"//tbody//tr[{k}]//div/div[1]/div[2]/div[2]/div[1]/p").click()
            time.sleep(3)
            up = context.driver.find_element(By.XPATH,
                                             "//app-activity/div/div[2]/div[1]/div[1]/div/div/div/div/div/p").text
            if "Task updated by" in up:
                flag = True
                break
            else:

                flag = False
    assert flag


@when(u'go on opportunities')
def step_impl(context):
    act = ActionChains(context.driver)
    (act
     .move_to_element(context.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))
     .move_to_element(context.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunities'])"))
     .click()
     .perform())
    time.sleep(3)


# @when(u'create task enter details')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, "//app-tasks-list/div[1]/div[1]/div[2]/button").click()
#     context.TP = TasksPage(context.driver)
#
#     context.TP.enterTaskDetails("hello", "1345")
#     context.TP.clickOnTaskSave()
#
#
# @when(u'click clear all and filter tomorrow')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, "//app-tasks-list[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
#     time.sleep(3)
#     context.driver.find_element(By.XPATH, "//div[2]/div/div[1]/div/div[3]/div/div/button[1]").click()
#     context.driver.find_element(By.XPATH, "//label[normalize-space()='Tomorrow']").click()
#     time.sleep(3)
#
#
# @Then(u'validate Not Associated is displaying or not')
# def step_impl(context):
#     c = context.driver.find_element(By.XPATH, "(//p[@class='text-xs text-red-500 text-left'])[1]").text
#     assert "Not Associated" == c
#
# @when(u'collect one phone number')
# def step_impl(context):
#     global number
#     #clear all clicking
#     context.driver.find_element(By.XPATH, "//app-tasks-list[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
#     time.sleep(3)
#
#     number = context.driver.find_element(By.XPATH,"(//div[1]/div[2]/div[2]/div[2]/p)[2]").text.split()
#
#
#
# @when(u'send input this number in search field')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"//input[@id='search']").send_keys(number[1],Keys.ENTER)
#     time.sleep(3)
#
# @Then(u'find the users with this numbers got displayed or not')
# def step_impl(context):
#     flag=True
#     numbers=context.driver.find_elements(By.XPATH,"//div[1]/div[2]/div[2]/div[2]/p")
#     for i in numbers:
#         if number[1] in i.text:
#             flag=True
#         else:
#             flag=False
#             break
#     assert flag
#
#
# @when(u'click on clone option of task')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[2]//*[name()='svg']").click()
#     context.driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[2]//*[name()='svg']//following::p[@id='menu-item-0']").click()
#     time.sleep(2)
#     context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
#     time.sleep(2)
#
# @Then(u'validate in activity area')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"(//div[@class='items-center ml-2 text-red-500'])[1]").click()
#     time.sleep(3)
#     v=context.driver.find_element(By.XPATH,"(//p[@class='font-medium text-sm ng-star-inserted'])[1]").text
#     assert "Task created by" in v or "Site Visit created by" in v
#
#
#
# @when(u'click on task bar and add comment')
# def step_impl(context):
#     global comment
#     context.driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]/p").click()
#     time.sleep(2)
#
#     comment="hello"
#     context.driver.find_element(By.XPATH,"//input[@name='comment']").send_keys(comment)
#     context.driver.find_element(By.XPATH,"//button[normalize-space()='Post']").click()
#     time.sleep(2)
#
# @Then(u'validate the commnet added or not')
# def step_impl(context):
#     v=context.driver.find_element(By.XPATH,"//div[2]/div[6]/div/div[2]/p").text
#     context.driver.find_element(By.XPATH,"//form/div/div[1]/div[1]/div[2]/button//*[name()='svg']").click()
#     # context.driver.execute_script("arguments[0].click()",b)
#     time.sleep(3)
#     assert v == comment