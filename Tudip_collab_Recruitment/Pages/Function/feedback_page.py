import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
from Pages.Locators.feedback_Locator import feedbacklocator
from helper import helper as h
class feedback_page:
        def __init__(self, page:Page):
            self.page = page
            self.feedback=feedbacklocator()
            self.helperobject=h()
        def written(self,marks_obtain):
            self.page.locator(self.feedback.written_Locator("Written")).click()
            self.page.locator(self.feedback.marks_Locator()).fill(marks_obtain)
            self.page.locator(self.feedback.add_Locator()).click()
            popupmsg=self.page.get_by_label("Feedback added successfully.")
            self.helperobject.checkvisible(popupmsg)
            # expect(popupmsg).to_be_visible()
            feedbackresult=self.page.locator(self.feedback.feedbackshow_Locator())
            expect(feedbackresult).to_be_visible()
            self.page.get_by_title("Delete feedback").click()
            self.page.get_by_role("button", name="Delete").click()
            deletemsg=self.page.get_by_label("Feedback deleted successfully.")
            # expect(deletemsg).to_be_visible()
            self.helperobject.checkvisible(deletemsg)
        # def Notes(self):
        #      self.page.locator(self.feedback.written_Locator("Notes")).click()

            
