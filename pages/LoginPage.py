from selenium.webdriver.common.by import By

from pages.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    email_XPATH="//input[@id='email']"
    password_ID="examplePassword0"
    signIn_XPATH="//button[normalize-space()='Sign in']"

    def enter_mail_and_password(self,mail,password):
        self.driver.find_element(By.XPATH,self.email_XPATH).clear()
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(mail)
        self.driver.find_element(By.ID, self.password_ID).clear()
        self.driver.find_element(By.ID, self.password_ID).send_keys(password)
    def clickSignIn(self):
        self.driver.find_element(By.XPATH,self.signIn_XPATH).click()
        return DashboardPage(self.driver)