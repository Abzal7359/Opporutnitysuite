import configparser
import time

from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ConvertStatusPage import ConvertStatusPage
from pages.kanbanViewPage import KanbanViewPage

config = configparser.ConfigParser()
config.read(r'config.txt')




@when(u'get text of stage')
def step_impl(context):
    context.KVP=KanbanViewPage(context.driver)
    context.KVP.get_text()



@when(u'drag and drop from one stage')
def step_impl(context):
    context.KVP.drag_and_drop_oneStage()


@when(u'validate it is dropped or not')
def step_impl(context):
    assert context.KVP.valiadte_is_dropped()
    # ll=[]

@when(u'click back to kanban _view')
def step_impl(context):
    context.KVP = KanbanViewPage(context.driver)
    context.KVP.click_back_kanban()



@when(u'select one element drag and drop into won status')
def step_impl(context):
    context.KVP.drag_into_won()


@when(u'check it is dropped or not')
def step_impl(context):
    assert context.KVP.is_dropped_or_not()


#code to drag and drop into lost status
lost=[]
@when(u'select one element drag and drop into lost status')
def step_impl(context):
    action = ActionChains(context.driver)
    context.driver.execute_script("arguments[0].scrollIntoView(true)",
                               context.driver.find_element(By.XPATH, "//app-kanban/div/div/div[9]/div[1]/span"))
    actu =context.driver.find_element(By.XPATH, "//app-kanban/div/div/div[7]/div[3]/div[1]/div/div/div[2]/p[1]").text
    lost.append(actu)
    sc = context.driver.find_element(By.XPATH, "//app-kanban/div/div/div[7]/div[3]/div[1]/div")
    ta=context.driver.find_element(By.XPATH,"(//app-kanban/div/div/div[8]/div[3]/div/div)[1]")
    time.sleep(float(config.get('waiting_time', 'min_wait')))
    (action
     .click_and_hold(sc)

     .move_to_element(ta)
     .release(ta))
    action.perform()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))

@when(u'enter lost reason and click save')
def step_impl(context):
    context.csp=ConvertStatusPage(context.driver)
    time.sleep(float(config.get('waiting_time', 'min_wait')))
    context.csp.enter_lost_reason_text("not interseted")
    context.csp. click_savee_button()




@Then(u'check it dropped into lost or not')
def step_impl(context):
    ss=[]
    expect=context.driver.find_element(By.XPATH,"(//app-kanban/div/div/div[8]/div[3]/div[1]//p)[1]").text
    if lost[0]==expect:
        ss.append(True)

    yy = context.driver.find_element(By.XPATH, "//app-kanban/div/div/div[8]/div[1]/span").text
    context.driver.find_element(By.XPATH, "(//app-kanban/div/div/div[8]/div[3]/div[1]//p)[1]").click()
    time.sleep(3)

    lst=context.driver.find_element(By.XPATH,
                                          "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text

    if "Opportunity stage changed" and yy in lst:
        ss.append(True)

    else:
        ss.append(False)

    if False not in ss:
        context.driver.find_element(By.XPATH,"//span[normalize-space()='Opportunity']").click()
        time.sleep(4)
        wait = WebDriverWait(context.driver, 10)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[1]//*[local-name()='svg']")))
        element.click()
        time.sleep(3)
        assert True
    else:
        context.driver.find_element(By.XPATH, "//span[normalize-space()='Opportunity']").click()
        time.sleep(4)
        wait = WebDriverWait(context.driver, 10)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[1]//*[local-name()='svg']")))
        element.click()
        time.sleep(3)
        assert False