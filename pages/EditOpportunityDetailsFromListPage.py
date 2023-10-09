import time

from selenium.webdriver.common.by import By


class EditOpportunityDetailsFromListPage:
    def __init__(self,driver):
        self.driver=driver

    OPPORTUNITY_LINK = (By.XPATH, "(//span[normalize-space()='Opportunity'])[1]")
    STAGE_COLUMN = (By.XPATH, "//tbody/tr[1]/td[6]/div[1]/span[1]")
    STAGE_OPTION = (By.XPATH, "//label[normalize-space()='Initial Call']")
    OPPORTUNITY_ROW = (By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]")
    ACTIVITY_TEXT = (By.XPATH, "//div[@class='ng-star-inserted']//p")
    LABELS_COLUMN = (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/span[1]")
    CHECKBOXES = (By.XPATH, "(//input[contains(@id,'selectedItem')])")
    LABEL_HEADER = (By.XPATH, "//th[text()=' LABEL ']")
    OPPORTUNITY_OWNER_COLUMN = (By.XPATH, "//tbody/tr[1]/td[9]/div[1]/span[1]")
    LABELS = (By.XPATH, "//label[contains(normalize-space(),'')]")

    def change_opportunity_owner_and_validate(self):
        Expecttext = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[9]/div[1]/span[1]").text
        actuall = ""
        opportunity_owner_column = self.driver.find_element(*self.OPPORTUNITY_OWNER_COLUMN)
        opportunity_owner_column.click()
        time.sleep(2)
        labels = self.driver.find_elements(*self.LABELS)
        for i in range(1, len(labels)):
            if labels[i].text.lower() != Expecttext.lower():
                actuall = labels[i].text
                labels[i].click()
                break
            else:
                pass
        time.sleep(3)
        self.driver.find_element(*self.OPPORTUNITY_ROW).click()
        time.sleep(3)
        expect = f"Opportunity assigned from {Expecttext} to {actuall}"
        t = self.driver.find_element(*self.ACTIVITY_TEXT).text
        if expect.lower() in t.lower():
            return True
        else:
            return False



    def click_opportunity_link(self):
        opportunity_link = self.driver.find_element(*self.OPPORTUNITY_LINK)
        opportunity_link.click()
        time.sleep(3)

    def select_stage_option(self):
        stage_column = self.driver.find_element(*self.STAGE_COLUMN)
        stage_column.click()
        stage_option = self.driver.find_element(*self.STAGE_OPTION)
        stage_option.click()
        time.sleep(3)


    def is_stage_change(self):
        lead_row = self.driver.find_element(*self.OPPORTUNITY_ROW)
        lead_row.click()
        time.sleep(3)
        actuallText = self.driver.find_element(*self.ACTIVITY_TEXT).text
        if "stage changed" and "Initial Call" in actuallText:
            return True
        else:
            return False

    def change_labels(self):
        labels_column = self.driver.find_element(*self.LABELS_COLUMN)
        labels_column.click()
        time.sleep(2)
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        for i in range(1, len(checkboxes)):
            if checkboxes[i].is_selected():
                self.driver.execute_script("arguments[0].click()", checkboxes[i])
                time.sleep(3)
                checkboxes = self.driver.find_elements(*self.CHECKBOXES)  # Refresh the checkboxes
            else:
                self.driver.execute_script("arguments[0].click()", checkboxes[i])
                time.sleep(3)
                checkboxes = self.driver.find_elements(*self.CHECKBOXES)  # Refresh the checkboxes
        self.driver.find_element(*self.LABEL_HEADER).click()

    def validate_activity_area_labels_changed(self):
        opportunity_row = self.driver.find_element(*self.OPPORTUNITY_ROW)
        opportunity_row.click()
        time.sleep(3)
        actual_text = self.driver.find_element(*self.ACTIVITY_TEXT).text

        if "Opportunity label(s)" in actual_text:
            return True
        else:
            return False