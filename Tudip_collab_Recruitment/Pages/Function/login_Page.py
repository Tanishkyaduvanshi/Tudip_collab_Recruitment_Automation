import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
from Pages.Locators.login_Locators import Locate 
from dotenv import load_dotenv
from helper import helper as h
import os

load_dotenv()
class login_Page:
        def __init__(self, page:Page):
            self.page = page
            self.helperobj=h()
        # Navigation page url
        def navigation(self):        
                # login_page_url = data['URLs']['loginpageurl']
                login_page_url = os.getenv("pageurl")
                self.page.goto(login_page_url)
                expect(self.page).to_have_url("http://dev.recruitment.tudip.uk/#/career")
        def login_user(self):
        # Username field
                username =self.page.locator(Locate.username_locator("Email")).nth(1)
                username.fill(os.getenv("loginusername"))
                self.helperobj.checkvisible(username)
                # expect(username).to_be_visible()
        #  Password filed
                password =self.page.locator(Locate.username_locator("Password (min. 4 characters)")).nth(1)
                password.fill(os.getenv("loginpassword"))
                self.helperobj.checkvisible(password)
                # expect(password).to_be_visible()
        # Login button
                login=self.page.locator(Locate.login_locator()).nth(1)
                login.click()


