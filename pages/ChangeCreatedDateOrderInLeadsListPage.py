import time

from selenium.webdriver.common.by import By
from datetime import datetime

class ChangeCreatedDateOrderInLeadsListPage:
    def __init__(self,driver):
        self.driver=driver

    DESCENDING_DATE_BUTTON = (By.XPATH, "(//*[name()='svg'][@id='sort-as-usual'])[1]")
    CREATEDDATE_HEADER = (By.XPATH, "(//span[@class='w-auto ng-star-inserted'][normalize-space()='CREATED DATE'])[1]")
    CREATED_DATE_COLUMN = (By.XPATH, "//tbody/tr/td[12]")

    ASCENDING_DATE_BUTTON = (By.XPATH, "(//*[name()='svg'][@id='sort-decending'])[1]")

    def click_descending_date_button(self):
        descending_date_button = self.driver.find_element(*self.DESCENDING_DATE_BUTTON)
        descending_date_button.click()
        time.sleep(3)
        created_date_header = self.driver.find_element(*self.CREATEDDATE_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", created_date_header)

    def click_descending_date_buttonn(self):
        descending_date_button = self.driver.find_element(*self.DESCENDING_DATE_BUTTON)
        descending_date_button.click()
        time.sleep(3)
        created_date_header = self.driver.find_element(By.XPATH,"//th[text()=' CREATED DATE ']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", created_date_header)





    def click_ascending_date_button(self):
        ascending_date_button = self.driver.find_element(*self.ASCENDING_DATE_BUTTON)
        ascending_date_button.click()
        time.sleep(3)
        created_date_header = self.driver.find_element(*self.CREATEDDATE_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", created_date_header)

    def click_ascending_date_buttonn(self):
        ascending_date_button = self.driver.find_element(*self.ASCENDING_DATE_BUTTON)
        ascending_date_button.click()
        time.sleep(3)
        created_date_header = self.driver.find_element(By.XPATH,"//th[text()=' CREATED DATE ']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", created_date_header)





    def is_in_ascendingOrder(self):
        l = self.driver.find_elements(*self.CREATED_DATE_COLUMN)
        z = []
        for i in range(len(l)):
            z.append(l[i].text)
            if len(z) > 1:
                if z[0] == z[1]:
                    z.pop(0)
                else:
                    break

        date_format = "%b %d, %Y"
        date1 = datetime.strptime(z[0], date_format)
        date2 = datetime.strptime(z[1], date_format)

        # Compare the datetime objects
        if date1 < date2:
            self.driver.find_element(By.XPATH, "(//*[name()='svg'][@id='sort-ascending'])[1]").click()
            time.sleep(3)
            return True
        else:
            self.driver.find_element(By.XPATH, "(//*[name()='svg'][@id='sort-ascending'])[1]").click()
            time.sleep(3)
            return False







    def is_in_descendingOrder(self):

        l = self.driver.find_elements(*self.CREATED_DATE_COLUMN)
        z = []
        for i in range(len(l)):
            z.append(l[i].text)
            if len(z) > 1:
                if z[0] == z[1]:
                    z.pop(0)
                else:
                    break

        date_format = "%b %d, %Y"
        date1 = datetime.strptime(z[0], date_format)
        date2 = datetime.strptime(z[1], date_format)

        # Compare the datetime objects
        if date1 > date2:
            return True
        else:
            return False






