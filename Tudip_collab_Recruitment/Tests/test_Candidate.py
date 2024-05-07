import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from Pages.Function.candidate_page import candidate_page
from playwright.sync_api import Page
from helper import helper as h
class Test_form:
    def __init__(self, page: Page):
        self.page = page
        self.helperobj = h()  # Creating an instance of the helper class
    def form(self):
        # Using the helper object to call the json_Data() method
        data = self.helperobj.json_Data()
        # Now 'data' contains the JSON data from config.json
        formpage = candidate_page(self.page)
        formpage.candidate_form()
        formpage.button()
        formpage.first_Name(data["form_Alldetails"]["firstname"])
        formpage.last_name(data["form_Alldetails"]["lastname"])
        formpage.email(data["form_Alldetails"]["email"])
        formpage.contact_number(data["form_Alldetails"]["conatct"])
        formpage.highest_Qualification()
        formpage.subject()
        formpage.Position()
        formpage.experience()
        formpage.calander_Icon()
        formpage.calander_Textarea()
        formpage.active_Nonactive()
        formpage.resume_upload()
        formpage.submit_Btn()
        formpage.icon_person()
        
