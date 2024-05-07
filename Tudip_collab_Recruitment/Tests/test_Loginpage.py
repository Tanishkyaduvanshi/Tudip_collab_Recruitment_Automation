import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from Pages.Function.login_Page import login_Page
from playwright.sync_api import Page


class Test_login:
    def __init__(self, page: Page):
        self.page = page
    def test_loginFunction(self):
        loginNow = login_Page(self.page)        
        loginNow.navigation()
        loginNow.login_user()
        
        

