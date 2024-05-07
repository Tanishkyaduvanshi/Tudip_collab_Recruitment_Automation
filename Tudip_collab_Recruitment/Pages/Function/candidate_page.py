import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
from Pages.Locators.candidate_Locator import candidate_Locator 
from helper import helper as h
class candidate_page:
        def __init__(self, page:Page):
            self.page = page
            self.helperobj=h()
            self.locatorobj=candidate_Locator()
        def candidate_form(self):
            # pop up message for login Successfull
            message=self.page.locator(self.locatorobj.msg())
            # Assertion if the pop up is visible or not
            self.helperobj.checkvisible(message)
            # wait for time out for popup to be disappear
            self.page.wait_for_timeout(4000)
            # candidate btn
        def button(self):
            btn=self.page.locator(self.locatorobj.candidatebtn())
            self.helperobj.checkvisible(btn)
            btn.click()
        # first name to be entered
        def first_Name(self,firstname):
            Name=self.page.locator(self.locatorobj.detail_Locator("first_name"))
            Name.fill(firstname)
            self.helperobj.notempty(Name)
        # Last name to be entered
        def last_name(self,surname):
            lastname=self.page.locator(self.locatorobj.detail_Locator("last_name"))
            lastname.fill(surname)
            self.helperobj.notempty(lastname)
        # Email to be entered
        def email(self,full_email):
            Email=self.page.locator(self.locatorobj.detail_Locator("email"))
            Email.fill(full_email)
            self.helperobj.notempty(Email)
        # contact to be entered
        def contact_number(self,contact_numbers):
            Contact=self.page.locator(self.locatorobj.detail_Locator('phone_no'))
            Contact.fill(contact_numbers)
            self.helperobj.notempty(Contact)
        #  Highest Qualification 
        def highest_Qualification(self):
            self.page.locator(self.locatorobj.dropdown_Locator()).select_option(value="15")
                # Choose Subject from the 
        def subject(self):
             self.page.locator(self.locatorobj.subject_Locator()).select_option(value="PCM")
        #  Select position from the options
        def Position(self):
            self.page.locator(self.locatorobj.position_Locator()).select_option(value="84")
        #  Experience of work
        def experience(self):
            self.page.locator(self.locatorobj.experience_Locator()).select_option(value="53")
        def calander_Icon(self):
             self.page.locator(self.locatorobj.calander_Icon_locator()).click()
        def calander_Textarea(self):
             DOB=self.helperobj.json_Data()
             self.page.locator(self.locatorobj.calander_Textarea_locator()).fill(DOB["Dob"])
             self.page.keyboard.press("Enter")
        def active_Nonactive(self):
            self.page.locator(self.locatorobj.active_Locator()).select_option(value="Active")
        def resume_upload(self):
            input=self.page.locator(self.locatorobj.remuse_Locator())
            resumelocation=self.helperobj.json_Data()
            input.set_input_files(resumelocation["resume"])
        def submit_Btn(self):
            self.page.locator(self.locatorobj.submitbtn()).click()
        def icon_person(self):
            self.page.locator(self.locatorobj.iconperson_Locator()).click()



