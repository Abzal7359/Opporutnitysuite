import time

from selenium.webdriver.common.by import By


class ApplyinFilter_InOpportunityPage:
    def __init__(self,driver):
        self.driver=driver

    FILTERS_MENU = (By.XPATH, "(//span[normalize-space()='Filters'])[1]")

    def isDefault_in_openFilter(self):
        l = ["Open", "Won","Lost"]
        ll=self.driver.find_elements(By.XPATH,"//tbody//tr")
        flag = True
        for i in range(1, (len(ll)+1)):
            #the below xpath to loop on status column
            z = f"//tbody/tr[{i}]/td[7]/span[1]"
            c = self.driver.find_element(By.XPATH, z).text
            if c in l:
                pass
            else:
                flag = False
        return flag

    def click_add_filters_button(self):
        filters_menu = self.driver.find_element(*self.FILTERS_MENU)
        filters_menu.click()
        time.sleep(2)