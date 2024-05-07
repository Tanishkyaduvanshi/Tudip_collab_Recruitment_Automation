import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
from Pages.Locators.edit_Info import edit_Info as e
from helper import helper as h
class edit_Infopage:
        def __init__(self, page:Page):
            self.page = page
            self.edit_Information=e()
            self.helperobject=h()
        def name_Edit(self):
           Name = self.page.locator(self.edit_Information.edit_namelocator())
           Name.clear()
           edit_data = self.helperobject.json_Data()
           Name.fill(edit_data["editdata"]) 
           self.page.locator(self.edit_Information.edit_Submit()).click()
        def message(self):
          messageupate=self.page.locator(self.edit_Information.popup_message())
          self.helperobject.checkvisible(messageupate)
        def editname_Search(self):
          Name=self.page.locator(self.edit_Information.searcheditname_Locator())
          editdata=self.helperobject.json_Data()
          Name.fill(editdata["editdata"])
        def Show_btn(self):
             self.page.locator(self.edit_Information.showbtn()).click()
        # verify the table is remains
        def tablename(self):
            data = self.helperobject.json_Data()
            for column_name in data["column"]:
                col_Name = self.page.get_by_role("cell", name=column_name.strip())
                expect(col_Name).to_be_visible()
                col_inner_text=col_Name.inner_text()
                if col_inner_text=="Name":
                    name_detail = self.page.get_by_text(data["editdata"]).nth(1)
                    editdata=self.helperobject.json_Data()
                    expect(name_detail).to_contain_text(editdata["editdata"])


        def feedbackicon(self):
          self.page.locator(self.edit_Information.feedback_Locator()).nth(0).click()