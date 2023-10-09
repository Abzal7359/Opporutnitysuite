import time

from selenium.webdriver.common.by import By


class ApplyingFilterCreateTab:
    def __init__(self,driver):
        self.driver=driver

    FILTERS_MENU = (By.XPATH, "(//span[normalize-space()='Filters'])[1]")
    ADD_FILTERS_BUTTON = (By.XPATH, "(//button[normalize-space()='Add Filters'])[1]")
    CREATE_TAB_BUTTON = (By.XPATH, "(//button[normalize-space()='Create Tab'])[1]")
    TAB_NAME_INPUT = (By.XPATH, "(//input[@placeholder='Enter filter name'])[1]")
    CREATE_BUTTON = (By.XPATH, "(//button[normalize-space()='Create'])[1]")
    CREATED_TAB_NAME_NUMBEROFLEADS= (By.XPATH, "(//h6[contains(normalize-space(),'')])[12]")
    FOOTER_NUMBEROFLEADS= (By.XPATH, "//div[@class='sm:flex sm:flex-1 sm:items-center sm:justify-between']//span[3]")
    NEW_FILTER_TAB = (By.XPATH, "(//div[@class='flex items-center cursor-pointer whitespace-nowrap'])[6]")
    OPTIONS_FILTER_BUTTON = (By.XPATH, "(//*[name()='svg'][@class='cursor-pointer h-4 more-icon-0 w-5'])[1]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "(//button[normalize-space()='YES'])[1]")
    FILTER_TABS = (By.XPATH, "//div[@class='flex items-center cursor-pointer whitespace-nowrap']")
    RENAME_TAB=(By.XPATH,"(//p[@class='text-sm mb-2'])[1]")
    EDIT_TAB_NAME_INPUT="(//input[@placeholder='Enter name'])[1]"
    RENAME_BUTTON = (By.XPATH, "(//button[normalize-space()='Rename'])[1]")

    def edit_new_filter_name(self):
        self.driver.find_element(By.XPATH, "(//div[@class='flex items-center cursor-pointer whitespace-nowrap'])[6]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='cursor-pointer h-4 more-icon-0 w-5'])[1]").click()
        self.driver.find_element(By.XPATH, "(//p[@class='text-sm mb-2'])[1]").click()
        self.driver.find_element(By.XPATH, "(//input[@placeholder='Enter name'])[1]").clear()
        namee = "edited"
        self.driver.find_element(By.XPATH, "(//input[@placeholder='Enter name'])[1]").send_keys(namee)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Rename'])[1]").click()
        time.sleep(2)

        filtername = self.driver.find_element(*self.NEW_FILTER_TAB).text

        if namee in filtername :
            return True
        else:
            return False





    def isDefault_in_openFilter(self):
        l = ["Active", "Not Contacted"]
        flag = True
        leng=self.driver.find_elements(By.XPATH,"//tbody//tr")

        for i in range(1, (len(leng)+1)):
            #the below xpath to loop on status column
            z = f"//tbody/tr[{i}]/td[9]/span[1]"
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
        add_filters_button = self.driver.find_element(*self.ADD_FILTERS_BUTTON)
        add_filters_button.click()

    def select_filter_type(self,selectAttribute,selectValues):
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='rotate-0 h-5 w-5 transform'])[1]").click()
        tt =selectAttribute                     #"Sub"
        source = f"(//label[contains(normalize-space(),'{tt}')])[1]"
        self.driver.find_element(By.XPATH, source).click()
        self.driver.find_element(By.XPATH, "(//span[@class='text-gray-900 mr-1 p-1 rounded ng-star-inserted'])[1]").click()
        type =selectValues                                      #"Face"
        source_type = f"(//label[contains(normalize-space(),'{type}')])[1]"
        self.driver.find_element(By.XPATH, source_type).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='rotate-0 h-5 w-5 transform'])[3]").click()

    def click_create_tab(self):
        create_tab_button = self.driver.find_element(*self.CREATE_TAB_BUTTON)
        create_tab_button.click()

    def enter_tab_name(self, tab_name):
        tab_name_input = self.driver.find_element(*self.TAB_NAME_INPUT)
        tab_name_input.send_keys(tab_name)

    def click_create_button(self):
        create_button = self.driver.find_element(*self.CREATE_BUTTON)
        create_button.click()
        time.sleep(5)

    def is_TAB_Created(self):
        e = self.driver.find_element(*self.FOOTER_NUMBEROFLEADS).text
        if int(e)==0:
            pass

        else:
            d = self.driver.find_element(*self.CREATED_TAB_NAME_NUMBEROFLEADS).text

        if int(e)==0:
            time.sleep(3)
            return True
        elif d == e:
            return True


        else:
            time.sleep(3)
            return False

    def is_TAB_Createdd_in_opportunity(self):
        new_filter_tab = self.driver.find_element(By.XPATH, "//*[@id='opportunity-filters']/div/div[2]/div[2]/div")
        new_filter_tab.click()
        time.sleep(2)
        d = self.driver.find_element(By.XPATH,"(//h6[contains(normalize-space(),'')])[10]").text
        e = self.driver.find_element(*self.FOOTER_NUMBEROFLEADS).text
        if d == e:
            time.sleep(3)
            return True

        else:
            time.sleep(3)
            return False




    def click_delete_filter(self):
        time.sleep(3)
        new_filter_tab = self.driver.find_element(*self.NEW_FILTER_TAB)
        new_filter_tab.click()
        time.sleep(3)
        options_filter_button = self.driver.find_element(*self.OPTIONS_FILTER_BUTTON)
        options_filter_button.click()
        self.driver.find_element(By.XPATH, "(//p[@class='text-sm'])[1]").click()
        confirm_delete_button = self.driver.find_element(*self.CONFIRM_DELETE_BUTTON)
        confirm_delete_button.click()
        time.sleep(3)

    def click_delete_filterr_in_opportunity(self):
        time.sleep(3)
        new_filter_tab = self.driver.find_element(By.XPATH,"//*[@id='opportunity-filters']/div/div[2]/div[2]/div")
        new_filter_tab.click()
        time.sleep(3)
        options_filter_button = self.driver.find_element(*self.OPTIONS_FILTER_BUTTON)
        options_filter_button.click()
        self.driver.find_element(By.XPATH, "(//p[@class='text-sm'])[1]").click()
        confirm_delete_button = self.driver.find_element(*self.CONFIRM_DELETE_BUTTON)
        confirm_delete_button.click()
        time.sleep(3)




    def is_FIlterTab_Delted(self):
        zl = self.driver.find_elements(*self.FILTER_TABS)
        if len(zl) == 5:
            return True
        else:
            return False


