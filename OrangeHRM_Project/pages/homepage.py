from OrangeHRM_Project.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    ADMIN = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[2]")
    PIM = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[3]")
    LEAVE = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[4]")
    TIME = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[5]")
    RECRUITMENT = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[6]")
    MYINFO = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[7]")
    PERFORMANCE = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[8]")
    DASHBOARD = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[9]")

    PERSONAL_DETAILS = (By.XPATH,"//a[normalize-space()='Personal Details']")
    CONTACT_DETAILS = (By.XPATH,"//a[normalize-space()='Contact Details']")
    EMERGENCY_CONTACTS = (By.XPATH,"//a[normalize-space()='Emergency Contacts']")
    DEPENDENTS = (By.XPATH,"//a[normalize-space()='Dependents']")
    IMMIGRATION = (By.XPATH,"//a[normalize-space()='Immigration']")
    JOB = (By.XPATH,"//a[contains(text(),'Job')]")
    SALARY = (By.XPATH,"//a[contains(text(),'Salary')]")
    REPORT = (By.XPATH,"//a[contains(text(),'Report')]")
    QUALIFICATIONS = (By.XPATH,"//a[contains(text(),'Quali')]")
    MEMBERSHIPS = (By.XPATH,"//a[contains(text(),'Mem')]")

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def is_admin_visible(self):
        return self.is_element_displayed(self.ADMIN)

    def is_pim_visible(self):
        return self.is_element_displayed(self.PIM)

    def is_leave_visible(self):
        return self.is_element_displayed(self.LEAVE)

    def is_time_visible(self):
        return self.is_element_displayed(self.TIME)

    def is_recrutiment_visble(self):
        return self.is_element_displayed(self.RECRUITMENT)

    def is_myinfo_visible(self):
        return self.is_element_displayed(self.MYINFO)

    def is_performance_visible(self):
        return self.is_element_displayed(self.PERFORMANCE)

    def is_dashboard_visible(self):
        return self.is_element_displayed(self.DASHBOARD)

    def click_myinfo(self):
        self.click_element(self.MYINFO)

    def is_personal_details_displayed(self):
        return self.is_element_displayed(self.PERSONAL_DETAILS)

    def is_contact_details_displayed(self):
        return self.is_element_displayed(self.CONTACT_DETAILS)

    def is_emergency_contacts_displayed(self):
        return self.is_element_displayed(self.EMERGENCY_CONTACTS)

    def is_dependents_displayed(self):
        return self.is_element_displayed(self.DEPENDENTS)

    def is_immigration_displayed(self):
        return self.is_element_displayed(self.IMMIGRATION)

    def is_job_displayed(self):
        return self.is_element_displayed(self.JOB)

    def is_salary_displayed(self):
        return self.is_element_displayed(self.SALARY)

    def is_report_displayed(self):
        return self.is_element_displayed(self.REPORT)

    def is_qualification_displayed(self):
        return self.is_element_displayed(self.QUALIFICATIONS)

    def is_membership_displayed(self):
        return self.is_element_displayed(self.MEMBERSHIPS)

    def click_personal_details(self):
        self.click_element(self.PERSONAL_DETAILS)

    def click_contact_details(self):
        self.click_element(self.CONTACT_DETAILS)

    def click_emergency_contacts(self):
        self.click_element(self.EMERGENCY_CONTACTS)

    def click_dependents(self):
        self.click_element(self.DEPENDENTS)

    def click_immigration(self):
        self.click_element(self.IMMIGRATION)

    def click_job(self):
        self.click_element(self.JOB)

    def click_salary(self):
        self.click_element(self.SALARY)

    def click_report(self):
        self.click_element(self.REPORT)

    def click_qualifications(self):
        self.click_element(self.QUALIFICATIONS)

    def click_memberships(self):
        self.click_element(self.MEMBERSHIPS)






