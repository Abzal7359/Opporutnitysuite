import time

from selenium.webdriver.common.by import By


class ChangeLabelsFromLeadsListPage:
    def __init__(self,driver):
        self.driver=driver

    LEAD_MENU = (By.XPATH, "(//span[normalize-space()='Lead'])[1]")
    LABELS_COLUMN = (By.XPATH, "//tbody/tr[1]/td[7]/div[1]/span[1]")
    LABEL_CHECKBOXES = (By.XPATH, "(//input[contains(@id,'selectedItem')])")
    EXPECTED_LABELS_TEXT = "Lead label(s)"

    def click_lead_menu(self):

        #-------------------------------------------------------------------
        lead_menu = self.driver.find_element(*self.LEAD_MENU)
        lead_menu.click()
        time.sleep(3)




    def changeLabels(self):
        labels_column = self.driver.find_element(*self.LABELS_COLUMN)
        labels_column.click()
        time.sleep(2)
        checkboxes = self.driver.find_elements(*self.LABEL_CHECKBOXES)
        for i in range(1, len(checkboxes)):
            if checkboxes[i].is_selected():
                self.driver.execute_script("arguments[0].click()", checkboxes[i])
                time.sleep(3)
                # this line to get ridd of stale element error
                checkboxes = self.driver.find_elements(*self.LABEL_CHECKBOXES)
            else:
                self.driver.execute_script("arguments[0].click()", checkboxes[i])
                time.sleep(3)
                # this line to get ridd of stale element error
                checkboxes = self.driver.find_elements(*self.LABEL_CHECKBOXES)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'LABEL')]").click()





    def are_labels_changed(self):
        self.driver.find_element(By.XPATH,"(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]").click()
        time.sleep(3)

        actuallText = self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//p").text

        if self.EXPECTED_LABELS_TEXT in actuallText:
            return True
        else:
            return False

