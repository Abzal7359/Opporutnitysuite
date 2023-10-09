import time

from selenium.webdriver.common.by import By


class AddDocumentPage:
    def __init__(self,driver):
        self.driver=driver

    DOCUMENT_OPTION = (By.XPATH, "//a[@id='document']")
    ADD_DOCUMENTS_BUTTON = (By.XPATH, "//button[normalize-space()='Add Documents']")
    FILE_UPLOAD_INPUT = (By.XPATH, "//input[@id='file-upload - ']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    UPLOADED_FILES = (By.XPATH, "//div[@class='flex flex-col ng-star-inserted']")

    def click_document_option(self):
        document_option = self.driver.find_element(*self.DOCUMENT_OPTION)
        self.driver.execute_script("arguments[0].click()", document_option)
        time.sleep(2)

    def click_add_documents_button(self):
        add_documents_button = self.driver.find_element(*self.ADD_DOCUMENTS_BUTTON)
        add_documents_button.click()
        time.sleep(2)

    def upload_file(self, file_path):
        file_input = self.driver.find_element(*self.FILE_UPLOAD_INPUT)
        file_input.send_keys(file_path)
        time.sleep(5)

    def click_save_button(self):
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        save_button.click()
        time.sleep(3)

    def check_uploaded_files(self):
        uploaded_files = self.driver.find_elements(*self.UPLOADED_FILES)
        return len(uploaded_files) >= 1