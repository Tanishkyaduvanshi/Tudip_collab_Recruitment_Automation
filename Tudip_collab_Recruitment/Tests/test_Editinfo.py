import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from Pages.Function.edit_Infopage import edit_Infopage
from Pages.Function.candidate_page import candidate_page
from Pages.Function.view_Candidate_page import view_Candidate_page
from Pages.Function.edit_Infopage import edit_Infopage
from playwright.sync_api import Page
from helper import helper as h

class Test_Editdetails:
    def __init__(self, page: Page):
        self.page = page
        self.helperobj = h()
    def editall_info(self):
        testedit = edit_Infopage(self.page)
        testobj2 = candidate_page(self.page)
        testobj3 = view_Candidate_page(self.page)
        testobj4= edit_Infopage(self.page)
        testedit.name_Edit() 
        testedit.message()
        testobj2.icon_person()
        data = self.helperobj.json_Data()
        testobj3.search_Icon(data["editdata"])
        testobj4.editname_Search()
        testobj4.Show_btn()
        testobj4.tablename()
        testobj4.feedbackicon()
        
