import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.TasksPage import TasksPage


class LeadsPage:
    def __init__(self,driver):
        self.driver=driver

    AddLead_XPATH="//div[@class='flex justify-between px-2' and text()=' Add Lead ']"

    #mandatory fields
    firstname_XPATH="//input[@id='first-name ']"
    lastname_XPATH="//input[@id='last-name']"
    email_XPATH="//input[@id='email']"
    mobileNumber_XPATH="//input[@id='phone-number']"
    AssignedTo_XPATH="(//button[contains(@class,'pr-3')])[3]"
    assigningPerson_XPATH="(//div[@class='flex items-center cursor-pointer p-2 ng-star-inserted'])[3]"         #"(//label[normalize-space()='kishor kharade'])[1]"
    campaign_XPATH="(//button[contains(@class,'pr-3')])[4]"
    campaignSelect_XPATH="(//div[@class='flex items-center cursor-pointer p-2 ng-star-inserted'])[3]"               #"(//label[normalize-space()='bajaj'])[1]"
    Labels_XPATH="(//button[contains(@class,'p-0')])[2]"
    RNR_XPATH="(//input[@id='selectedItem-1'])[1]"
    Description_XPATH="//textarea[@id='descriptionInfo']"


    save_XPATH="(//button[normalize-space()='Save'])[1]"
    Activity_text_area_XPATH="(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])"
    mail_validation_XPATH="//div[@class='mt-2']//p[@class='ng-star-inserted']"

    Tasks_XPATH="//a[@id='task']"

    #bulk actions multiple selection for changing assigne
    ASSIGN_LEAD_OWNER_BUTTON = (By.XPATH, "(//span[normalize-space()='Assign Lead Owner'])[1]")

    LEAD_OWNER_DROPDOWN = (By.XPATH, "(//button[@class='absolute inset-y-0 right-0 flex items-center pr-3'])[1]")
    LEAD_OWNER_OPTION = (By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[7]")
    SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
    expected=[]

    # bulk action mail sending
    SEND_EMAIL_BUTTON = (By.XPATH, "(//span[normalize-space()='Send Email'])[1]")
    SENDER_DROPDOWN = (By.XPATH, "//div/app-send-email/div/div/div/form/div[1]/div[2]/div[1]/div[1]")
    SENDER_OPTION = (
    By.XPATH, "//app-send-email/div/div/div/form/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]")
    SEND_BUTTON = (By.XPATH, "//app-send-email/div/div/div/form/div[1]/div[3]/div[2]")
    SUBJECT_INPUT = (By.XPATH, "//input[@placeholder='Subject']")
    OPEN_SELECTION_BUTTON = (By.XPATH, "(//button[@class='cursor-pointer bg-white border-[1px] ng-tns-c177-1'])[1]")
    FIRST_NAME_PLACEHOLDER = (By.XPATH, "//label[normalize-space()='First Name']")
    LAST_NAME_PLACEHOLDER = (By.XPATH, "//label[normalize-space()='Last Name']")
    FILE_INPUT = (By.XPATH, "//*[@id='file-upload - ']")
    ADDED_DOCUMENTS = (By.XPATH, "//*[contains(@id,'document')]/div[1]")
    DELETE_BUTTON = (By.XPATH, "//span[text()='Delete']")
    DELETE_ALERT_POPUP = (By.XPATH, "//app-notification-alert/div/div[2]/div/div")
    NO_BUTTON = (By.XPATH, "//button[normalize-space()='No']")
    SENDD_BUTTON = (By.XPATH, "//button[normalize-space()='Send']")
    MESSAGES_LINK = (By.XPATH, "//a[normalize-space()='Messages']")
    MESSAGES_TABLE = (By.XPATH, "//table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]")
    MESSAGE_COUNT = (By.XPATH, "//table[1]/tbody[1]/tr[1]/td[5]")

    def select_two_leads(self):
        global n
        n = 2
        for i in range(1, (1 + n)):
            z = f"//tbody/tr[{i}]/td[1]//input"
            self.driver.find_element(By.XPATH, z).click()

    def check_mail_isSent_or_not(self):
        self.driver.find_element(*self.MESSAGES_LINK).click()
        time.sleep(2)
        z = self.driver.find_element(*self.MESSAGES_TABLE).text
        zz = self.driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[1]/td[5]").text
        if z == "Sent" and int(zz) <= n:
            self.driver.find_element(By.XPATH, "(//a[normalize-space()='Leads'])[1]").click()
            return True
        else:
            self.driver.find_element(By.XPATH, "(//a[normalize-space()='Leads'])[1]").click()
            return False

    def click_send_button(self):
        send_button = self.driver.find_element(*self.SENDD_BUTTON)
        send_button.click()
        time.sleep(2)

    def is_delete_alert_displayed(self):
        s = self.driver.find_element(*self.DELETE_ALERT_POPUP).is_displayed()
        if s:
            self.driver.find_element(*self.NO_BUTTON).click()
            return True

    def click_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()

    def attach_document(self, file_path):
        file_input = self.driver.find_element(*self.FILE_INPUT)
        file_input.send_keys(file_path)

    def is_document_added(self):
        added_documents = self.driver.find_elements(*self.ADDED_DOCUMENTS)
        return len(added_documents) == 1

    def select_placeholders(self):
        self.driver.find_element(*self.OPEN_SELECTION_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME_PLACEHOLDER).click()
        self.driver.find_element(*self.OPEN_SELECTION_BUTTON).click()
        self.driver.find_element(*self.LAST_NAME_PLACEHOLDER).click()

    def is_popUp_displayed(self):
        c = self.driver.find_element(By.XPATH,
                                     "//div/app-send-email/div/div/div/form/div[1]/div[4]/div/div").is_displayed()
        return c

    def enter_subject(self, subject):
        subject_input = self.driver.find_element(*self.SUBJECT_INPUT)
        subject_input.clear()  # Clear any existing text
        subject_input.send_keys(subject)

    def select_sender(self):
        self.driver.find_element(*self.SENDER_DROPDOWN).click()
        self.driver.find_element(*self.SENDER_OPTION).click()
        self.driver.find_element(*self.SEND_BUTTON).click()

    def click_send_email_button(self):
        self.driver.find_element(*self.SEND_EMAIL_BUTTON).click()





    def click_assign_lead_owner_button(self):
        assign_lead_owner_button = self.driver.find_element(*self.ASSIGN_LEAD_OWNER_BUTTON)
        assign_lead_owner_button.click()



    def select_lead_owner(self):
        lead_owner_dropdown = self.driver.find_element(*self.LEAD_OWNER_DROPDOWN)
        lead_owner_dropdown.click()
        self.expected.append(self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[7]").text)
        #(//div[2]/app-select-dropdown/div/div/div/div/label)[7]
        #(//label[normalize-space()='Nitish Rana'])[1]
        lead_owner_option= self.driver.find_element(*self.LEAD_OWNER_OPTION)
        lead_owner_option.click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()

        time.sleep(5)



    def isAssignedLeader_Changed(self):
        val=[]
        for j in range(4):
            s = f"//tbody/tr[{j + 1}]/td[8]/div[1]/span[1]"
            actual = self.driver.find_element(By.XPATH, s).text
            if actual.lower() == self.expected[0].lower():
                val.append(True)
        if False not in val:
            return True
        else:
            return False

    #bulk actions multiple selection for adding labels
    ADD_LABEL_BUTTON = (By.XPATH, "//span[normalize-space()='Add Label']")
    LABEL_DROPDOWN = (By.XPATH, "(//button[@class='cursor-pointer bg-white w-full border-[1px] h-fit'])[1]")
    LABEL_ITEM = (By.XPATH, "//input[contains(@id,'selectedItem-0')]")
    SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Save'])[1]")

    def selectFourLeads(self):
        #code to birng leads in normal format from ascending order
        s=self.driver.find_element(By.XPATH,"(//span[@class='ml-5 cursor-pointer flex items-center ng-star-inserted'])[1]")
        self.driver.execute_script("arguments[0].click()",s)
        time.sleep(3)
        for i in range(4):
            z = f"//tbody/tr[{i + 1}]/td[1]//input"
            self.driver.find_element(By.XPATH, z).click()
    def selectFourLeadss(self):
        #code to birng leads in normal format from ascending order
        # s=self.driver.find_element(By.XPATH,"(//span[@class='ml-5 cursor-pointer flex items-center ng-star-inserted'])[1]")
        # self.driver.execute_script("arguments[0].click()",s)
        # time.sleep(3)
        for i in range(4):
            z = f"//tbody/tr[{i + 1}]/td[1]//input"
            self.driver.find_element(By.XPATH, z).click()

    def click_add_label_button(self):
        add_label_button = self.driver.find_element(*self.ADD_LABEL_BUTTON)
        add_label_button.click()
        time.sleep(2)
    def select_label_item(self):
        label_dropdown = self.driver.find_element(*self.LABEL_DROPDOWN)
        label_dropdown.click()
        label_item = self.driver.find_element(*self.LABEL_ITEM)
        label_item.click()
        time.sleep(2)
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        self.driver.execute_script("arguments[0].click()",save_button)
        time.sleep(3)

    def is_labels_selected(self):
        lists = []
        for j in range(4):
            path = f"//tbody/tr[{j + 1}]/td[7]/div[1]/span[1]"
            zz=self.driver.find_element(By.XPATH, path)
            self.driver.execute_script("arguments[0].click()",zz)
            # self.driver.find_element(By.XPATH, path).click()
            time.sleep(2)
            l = self.driver.find_elements(By.XPATH, "(//input[contains(@id,'selectedItem')])")
            for i in range(1, len(l)):
                if l[i].is_selected():
                    s = f"(//input[contains(@id,'selectedItem-{i - 1}')])/following-sibling::label"
                    t = self.driver.find_element(By.XPATH, s).text
                    if t == "Warmer":
                        lists.append(True)
                        self.driver.find_element(By.XPATH, "//span[contains(text(),'LABEL')]").click()
                        break
        if False not in lists:
            return True
        else:
            return False



    def is_labels_selectedd(self):
        lists = []
        for j in range(4):
            path = f"//tbody/tr[{j + 1}]/td[8]/div[1]/span[1]"
            zz=self.driver.find_element(By.XPATH, path)
            self.driver.execute_script("arguments[0].click()",zz)
            # self.driver.find_element(By.XPATH, path).click()
            time.sleep(2)
            l = self.driver.find_elements(By.XPATH, "(//input[contains(@id,'selectedItem')])")
            for i in range(1, len(l)):
                if l[i].is_selected():
                    s = f"(//input[contains(@id,'selectedItem-{i - 1}')])/following-sibling::label"
                    t = self.driver.find_element(By.XPATH, s).text
                    if t == "cold":
                        lists.append(True)
                        self.driver.find_element(By.XPATH, "//span[contains(text(),'LABEL')]").click()
                        break
        if False not in lists:
            return True
        else:
            return False



    def clickAddLead(self):
        # zz=self.driver.find_element(By.XPATH,"(//div[@class='flex justify-between px-2'])[1]")
        # self.driver.execute_script("arguments[0].click()",zz)
        self.driver.find_element(By.XPATH, self.AddLead_XPATH).click()


    def enter_Mandatory_Fields(self,firstName,lastname,email,mobile,description):

        w = WebDriverWait(self.driver, 7)
        f = w.until(expected_conditions.visibility_of_element_located((By.XPATH, self.firstname_XPATH)))
        f.clear()
        f.send_keys(firstName)
        self.driver.find_element(By.XPATH,self.lastname_XPATH).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(email)
        self.driver.find_element(By.XPATH, self.mobileNumber_XPATH).send_keys(mobile)
        self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Manual']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Word of mouth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.AssignedTo_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.assigningPerson_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.campaign_XPATH).click()

        self.driver.find_element(By.XPATH,self.campaignSelect_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.Labels_XPATH).click()
        self.driver.find_element(By.XPATH,self.RNR_XPATH).click()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click()",self.driver.find_element(By.XPATH, self.Labels_XPATH))
        # self.driver.find_element(By.XPATH, self.Labels_XPATH).click()
        self.driver.find_element(By.XPATH,self.Description_XPATH).send_keys(description)
        time.sleep(2)


    def clickAddLeadSave(self):
        self.driver.find_element(By.XPATH,self.save_XPATH).click()
        # time.sleep(2)

    def isLeadCreated(self,expect,expectmail):

        boolean = False
        l=self.driver.find_elements(By.XPATH, self.Activity_text_area_XPATH)
        for i in l:
            actuall = i.text
            Expected = expect
            if Expected in actuall:
                boolean = True
                break


        boolean_mail=False

        actuall_mail = self.driver.find_element(By.XPATH, self.mail_validation_XPATH).text
        Expected_mail = expectmail
        if Expected_mail in actuall_mail:
            boolean_mail=True

        l=[boolean,boolean_mail]
        if False not in l:
            return True
        else:
            return False


    def clickOnTasksPage(self):
        self.driver.find_element(By.XPATH, self.Tasks_XPATH).click()

        return TasksPage(self.driver)


