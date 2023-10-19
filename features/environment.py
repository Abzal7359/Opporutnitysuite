import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options
from pages.AddOpportunityDirectlyPage import AddOpportunityDirectlyPage
from pages.DashboardPage import DashboardPage

import configparser

config = configparser.ConfigParser()
config.read(r'config.txt')

url = config.get('global', 'production_url')
browser = config.get('global', 'browser_name')


def before_all(context):
    if browser == "edge":
        options = webdriver.EdgeOptions()
        # options.add_argument('--headless')
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        context.driver = webdriver.Edge(options=options)
    else:



        #______________________________________________________________________________________
        # options = webdriver.ChromeOptions()
        # options.add_argument("--disable-notifications")
        # options.add_experimental_option("detach", True)
        # context.driver = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     options=options
        # )

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(url)

    # -------------------------------------------------
    #
    # context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("masud.abdullah@bentolabs.io")
    # context.driver.find_element(By.XPATH, "(//input[@id='examplePassword0'])[1]").send_keys("Propflo@1234")
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    # time.sleep(3)
    # act = ActionChains(context.driver)
    # (act
    #  .move_to_element(context.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))
    #
    #  .move_to_element(context.driver.find_element(By.XPATH, "//a[normalize-space()='Opportunities']"))
    #  .click()
    #  .perform())
    # time.sleep(3)
    # context.driver.find_element(By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img").click()
    # time.sleep(3)
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunity Stages'])[1]").click()
    # #

    # context.AOD = AddOpportunityDirectlyPage(context.driver)
    # context.AOD.click_opportunities_link()
    # # # # # # #(//*[name()='svg'][@id='sort-as-usual'])[1]
    # time.sleep(3)
    # context.driver.find_element(By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]").click()
    # time.sleep(3)
    # context.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='w-6 h-6'])[2]").click()
    # time.sleep(5)


def after_all(context):
    context.DP = DashboardPage(context.driver)
    context.DP.clickSignout()
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
