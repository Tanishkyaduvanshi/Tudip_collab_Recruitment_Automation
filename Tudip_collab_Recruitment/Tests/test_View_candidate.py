import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
# from Pages.Function.candidate_page import candidate_page
from Pages.Function.view_Candidate_page import view_Candidate_page
from playwright.sync_api import Page
from helper import helper as h
class test_View_candidate:
    def __init__(self, page: Page):
        self.page = page
        self.helperobj = h()  # Creating an instance of the helper class
    def candidate_data(self):
        # Using the helper object to call the json_Data() method
        data = self.helperobj.json_Data()
        testobj = view_Candidate_page(self.page)
        testobj.search_Icon(data["search_for_candidate"])
        testobj.show_Btn()
        testobj.tablename(data["form_Alldetails"]["firstname"],data["form_Alldetails"]["email"])
        testobj.edit_Icon()
