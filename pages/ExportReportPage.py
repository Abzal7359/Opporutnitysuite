import time
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ExportReportPage:
    def __init__(self, driver):
        self.driver = driver

    EXPORT_BUTTON = (By.XPATH, "(//span[normalize-space()='Export'])[1]")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    REPORTS_MENU = (By.XPATH, "(//span[normalize-space()='Reports'])[1]")
    DOWNLOADS_LINK = (By.XPATH, "(//a[normalize-space()='Downloads'])[1]")
    REPORT_DATE_CELL = (By.XPATH, "//tbody/tr[1]/td[2]")

    def click_export_button(self):
        export_button = self.driver.find_element(*self.EXPORT_BUTTON)
        export_button.click()
        time.sleep(2)

    def select_export_column(self):
        for i in range(11):
            EXPORT_COLUMNS_CHECKBOXES = f"(//input[contains(@id,'sort-item-{i}')])"
            self.driver.find_element(By.XPATH, EXPORT_COLUMNS_CHECKBOXES).click()

    def click_SAVE_button(self):
        export_button = self.driver.find_element(*self.SAVE_BUTTON)
        export_button.click()
        time.sleep(5)

    def navigate_to_downloads_section(self):
        action = ActionChains(self.driver)
        reports_menu = self.driver.find_element(*self.REPORTS_MENU)
        downloads_link = self.driver.find_element(*self.DOWNLOADS_LINK)

        (action
         .move_to_element(reports_menu)
         .move_to_element(downloads_link)
         .click()
         .perform())
        time.sleep(3)

    def is_report_created(self):
        d = self.driver.find_element(*self.REPORT_DATE_CELL).text
        current_datetime = datetime.now()
        formatted_timestamp = current_datetime.strftime("%b%e, %Y")
        tex = self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]").text

        if "Lead Report" in tex or "Opportunity Report" in tex or d == formatted_timestamp:
            print(tex)
            print(d)
            return True
        else:
            print(tex)
            print(d,formatted_timestamp)
            return False
