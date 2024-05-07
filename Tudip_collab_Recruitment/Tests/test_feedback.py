import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
# from Pages.Function.candidate_page import candidate_page
from Pages.Function.feedback_page import feedback_page
from playwright.sync_api import Page
from helper import helper as h
class test_feedback:
    def __init__(self, page: Page):
        self.page = page
        self.helperobj = h()
    def feedback_form(self):
        self.testobj = feedback_page(self.page)
        data = self.helperobj.json_Data()
        self.testobj.written(data["marks_of_candidate"])
        