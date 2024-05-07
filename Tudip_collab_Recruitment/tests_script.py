import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright
from Tests.test_Loginpage import Test_login
from Tests.test_Candidate import Test_form
from Tests.test_View_candidate import test_View_candidate
from Tests.test_Editinfo import Test_Editdetails
from Tests.test_feedback import test_feedback
from conftest import set as page
from dotenv import load_dotenv
import os
load_dotenv()
def test_main(page):
# first page for login funcationality
        test_login = Test_login(page)   
        test_login.test_loginFunction()
# second page for form filling
        test_form = Test_form(page)
        test_form.form()
# Third page to show candidate data
        test_Candidatedata=test_View_candidate(page)
        test_Candidatedata.candidate_data()             
        page.wait_for_timeout(4000)
        Total_page=page.context.pages
        new_page=Total_page[1]
        new_page.bring_to_front()
# fourth page for edit information
        test_Information_edit = Test_Editdetails(new_page)
        test_Information_edit.editall_info()
# feedback pages
        Total_page=page.context.pages
        page.wait_for_timeout(4000)
        second_page=Total_page[2]
        second_page.bring_to_front()
        test_Feedback = test_feedback(second_page)
        test_Feedback.feedback_form()
        page.wait_for_timeout(3000)
        print("Done")
if __name__=="__main__":
    test_main(page)