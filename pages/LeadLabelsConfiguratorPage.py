import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from pages.DashboardPage import DashboardPage


class LeadLabelsConfiguratorPage:
    def __init__(self, driver):
        self.driver = driver

    LEAD_BUTTON = (By.XPATH, "(//a[text()='Leads'])[2]")
    ADD_LABEL_BUTTON = By.XPATH, "//div[text()=' Add Label ']"
    LABEL_INPUT = By.XPATH, "//input[@type='text']"
    LABEL_HEADER = By.XPATH, "//th[text()=' LABEL ']"
    LABEL_COUNT = By.XPATH, "//table/tbody/tr/td[1]/div//*[local-name()='svg']"
    SETTINGS_BACK = By.XPATH, "//div[text()='Settings']"
    LABEL_COLUMN = By.XPATH, "//table/tbody/tr[1]/td[7]/div"
    LABEL_COLUMN_IN_OPPORTUNITY=By.XPATH,"//table/tbody/tr[1]/td[8]/div"
    LABELS_IN_LEAD_LIST = By.XPATH, "//app-select-dropdown/div/div/div/div/label"
    SETTINGS_MENU = By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img"



    def click_opportunity_button(self):
        global before_count
        self.driver.find_element(By.XPATH, "(//a[text()='Opportunity'])[2]").click()
        before_count = len(self.driver.find_elements(*self.LABEL_COUNT))
    def click_lead_button(self):
        global before_count
        self.driver.find_element(*self.LEAD_BUTTON).click()
        before_count = len(self.driver.find_elements(*self.LABEL_COUNT))

    def click_add_label(self):
        self.driver.find_element(*self.ADD_LABEL_BUTTON).click()
        time.sleep(2)

    def enter_label_name(self):
        global label_name
        label_name = "close"
        self.driver.find_element(*self.LABEL_INPUT).send_keys(label_name)
        self.driver.find_element(*self.LABEL_HEADER).click()
        time.sleep(2)

    def validate_label_added(self):
        global after_count
        after_count = len(self.driver.find_elements(*self.LABEL_COUNT))
        return after_count > before_count

    def navigate_to_leads_list(self):
        DP = DashboardPage(self.driver)
        self.driver.find_element(*self.SETTINGS_BACK).click()
        time.sleep(3)
        DP.clickOnLeads()
        time.sleep(3)

    def navigate_to_opportunity_list(self):
        DP = DashboardPage(self.driver)
        self.driver.find_element(*self.SETTINGS_BACK).click()
        time.sleep(3)
        DP.clickOnOpportunities()
        time.sleep(3)




    def check_label_in_lead_list(self):
        self.driver.find_element(*self.LABEL_COLUMN).click()

        le = self.driver.find_elements(*self.LABELS_IN_LEAD_LIST)
        t = self.driver.find_element(By.XPATH, f"//app-select-dropdown/div/div/div/div[{len(le)}]/label").text
        return t == label_name

    def check_label_in_opportunity_list(self):
        self.driver.find_element(*self.LABEL_COLUMN_IN_OPPORTUNITY).click()

        le = self.driver.find_elements(*self.LABELS_IN_LEAD_LIST)
        t = self.driver.find_element(By.XPATH, f"//app-select-dropdown/div/div/div/div[{len(le)}]/label").text
        return t == label_name



    def go_to_leads_label_configurator(self):
        self.driver.find_element(*self.SETTINGS_MENU).click()
        time.sleep(2)
        self.driver.find_element(*self.LEAD_BUTTON).click()
        time.sleep(2)

    def change_label_position(self):
        sc = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{after_count}]/td[1]/div//*[local-name()='svg']")
        ta = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[1]/div//*[local-name()='svg']")
        action = ActionChains(self.driver)
        (action
         .click_and_hold(sc)
         .move_to_element(ta)
         .release(ta)
         .perform())
        time.sleep(2)

    def check_label_position(self):
        self.driver.find_element(*self.LABEL_COLUMN).click()
        t = self.driver.find_element(By.XPATH,
                                     f"//app-select-dropdown/div/div/div/div[{before_count + 1}]/label").text
        return t == label_name


    def check_label_position_in_Opportunity(self):
        self.driver.find_element(*self.LABEL_COLUMN_IN_OPPORTUNITY).click()
        t = self.driver.find_element(By.XPATH,
                                     f"//app-select-dropdown/div/div/div/div[{before_count + 1}]/label").text
        return t == label_name

    def delete_added_label(self):
        self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[3]//*[local-name()='svg']").click()
        time.sleep(2)

    def validate_label_deletion(self):
        global flag
        flag = True
        for i in range(before_count):
            tt = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[2]/div/span/span[1]").text
            if tt == label_name:
                flag = False
                break
        afterdel_count = len(self.driver.find_elements(*self.LABEL_COUNT))
        return (before_count == afterdel_count) and flag



    def disable_label(self):
        self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[1]/div/label").click()

    def check_label_disabled(self):
        self.driver.find_element(*self.LABEL_COLUMN).click()
        le_disbiling = len(self.driver.find_elements(*self.LABELS_IN_LEAD_LIST))
        return le_disbiling == before_count

    def check_label_disabled_in_opportunity(self):
        self.driver.find_element(*self.LABEL_COLUMN_IN_OPPORTUNITY).click()
        le_disbiling = len(self.driver.find_elements(*self.LABELS_IN_LEAD_LIST))
        return le_disbiling == before_count

    def enable_label(self):
        self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[1]/div/label").click()

    def check_label_enabled(self):
        self.driver.find_element(*self.LABEL_COLUMN).click()
        # self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[6]/div").click()

        le_enabiling = len(self.driver.find_elements(By.XPATH, "//app-select-dropdown/div/div/div/div/label"))
        return (le_enabiling == before_count + 1)

    def check_label_enabled_in_opportunity(self):
        self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[8]/div").click()

        le_enabiling = len(self.driver.find_elements(By.XPATH, "//app-select-dropdown/div/div/div/div/label"))
        return (le_enabiling == before_count + 1)

    def change_colour_label(self):
        global button_colour
        global label_text
        self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[2]/div/div/div").click()
        button_colour = self.driver.find_element(By.XPATH,
                                                 f"(//table/tbody/tr[{before_count}]/td[2]/div/div/div[2]/div)[14]").value_of_css_property(
            'background-color')
        self.driver.find_element(By.XPATH, f"(//table/tbody/tr[{before_count}]/td[2]/div/div/div[2]/div)[14]").click()
        time.sleep(1)
        label_text = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{before_count}]/td[2]/div/span").text.strip()

    def is_Colour_Applied(self):

        applied_color = self.driver.find_element(By.XPATH,
                                                 f"//table/tbody/tr[{before_count}]/td[2]/div/div/div").value_of_css_property(
            'background-color')

        self.navigate_to_leads_list()
        self.driver.find_element(*self.LABEL_COLUMN).click()
        # self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[6]/div").click()
        click_label = f"//label[normalize-space()='{label_text}']"
        self.driver.find_element(By.XPATH, click_label).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'LABEL')]").click()
        val = f"//tbody/tr[1]/td[7]/div/span/span[text()='{label_text}']"
        col = self.driver.find_element(By.XPATH, val).value_of_css_property('color')
        self.go_to_leads_label_configurator()

        return button_colour == applied_color and col in button_colour


    def is_Colour_Applied_in_opportunity(self):

        applied_color = self.driver.find_element(By.XPATH,
                                                 f"//table/tbody/tr[{before_count}]/td[2]/div/div/div").value_of_css_property(
            'background-color')

        self.navigate_to_opportunity_list()
        self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[8]/div").click()
        click_label = f"//label[normalize-space()='{label_text}']"
        self.driver.find_element(By.XPATH, click_label).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//table/thead/tr/th[7]").click()
        zz=label_text+" "
        val = f"//tbody/tr[1]/td[8]/div/span/span[text()='{zz}']"
        col = self.driver.find_element(By.XPATH, val).value_of_css_property('color')
        self.go_to_leads_label_configurator()

        return button_colour == applied_color and col in button_colour