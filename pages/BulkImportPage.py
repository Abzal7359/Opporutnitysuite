import csv
import time

from selenium.webdriver.common.by import By


class BulkImportPage:
    def __init__(self,driver):
        self.driver=driver

    BULK_IMPORT_ICON = (By.XPATH, "(//*[name()='svg'][@class='w-6 h-5'])[1]")
    BULK_IMPORT_OPTION = (By.XPATH, "(//a[normalize-space()='Bulk Import'])[1]")
    CSV_FILE_INPUT = (By.XPATH, "//div[@class='flex flex-col text-sm text-gray-600']//input")
    AUTO_SELECT_FIELDS=(By.XPATH, "(//input[@id='autoSelectFields'])[1]")
    VALIDATE_CSV=(By.XPATH, "(//button[normalize-space()='Validate CSV'])[1]")
    UPLOAD=(By.XPATH,"(//button[normalize-space()='Upload'])[1]")

    def click_bulk_import_option(self):
        self.driver.find_element(*self.BULK_IMPORT_ICON).click()
        self.driver.find_element(*self.BULK_IMPORT_OPTION).click()

    def upload_csv_file(self, file_path):
        self.driver.find_element(*self.CSV_FILE_INPUT).send_keys(file_path)


    def click_autoselect(self):
        self.driver.find_element(*self.AUTO_SELECT_FIELDS).click()
        self.driver.find_element(*self.VALIDATE_CSV).click()
        time.sleep(5)


    def click_TO_upload(self):
        self.driver.find_element(*self.UPLOAD).click()
        time.sleep(5)

    def check_Leads_added(self,file_path):
        l = []
        validate = []
        #code to read from xl file phone number and validate here
        with open(file_path, mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                # print(lines[4])
                if l:
                    l.append(lines[4])
                else:
                    l.append(1)
        for i in range(1, len(l)):
            path = f"(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[{i}]"
            self.driver.find_element(By.XPATH, path).click()
            number = "(//div[@class='flex text-blue-500 underline w-full']/span)[2]"
            if self.driver.find_element(By.XPATH, number).text in l:
                validate.append(True)
            else:
                validate.append(False)
        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Lead'])[1]").click()
        time.sleep(3)
        if False not in validate:
            return True
        else:
            return False
