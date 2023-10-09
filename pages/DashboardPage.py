import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.LeadsPage import LeadsPage


class DashboardPage:
    def __init__(self,driver):
        self.driver=driver

    sales_XPATH="//span[contains(text(),'Sales')]"
    lead_XPATH="//a[normalize-space()='Leads']"

    profile_XPATH = "(//div[@class='flex items-center cursor-pointer'])[1]"
    signout_button_XPATH = "(//a[normalize-space()='Sign Out'])[1]"

    def clickOnLeads(self):
        time.sleep(5)
        act = ActionChains(self.driver)
        (act
         .move_to_element(self.driver.find_element(By.XPATH, self.sales_XPATH))
         .move_to_element(self.driver.find_element(By.XPATH, self.lead_XPATH))
         .click()
         .perform())
        return LeadsPage(self.driver)
    def clickOnOpportunities(self):
        time.sleep(3)
        act = ActionChains(self.driver)
        (act
         .move_to_element(self.driver.find_element(By.XPATH, self.sales_XPATH))
         .move_to_element(self.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunities'])[1]"))
         .click()
         .perform())
        return LeadsPage(self.driver)


    def clickSignout(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.profile_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.signout_button_XPATH).click()
