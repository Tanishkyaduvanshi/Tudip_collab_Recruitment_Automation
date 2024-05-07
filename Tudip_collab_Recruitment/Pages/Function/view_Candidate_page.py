import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
from Pages.Locators.view_Candidate import view_Candidate
from helper import helper as h
class view_Candidate_page:
        def __init__(self, page:Page):
            self.page = page
            self.helperobject=h()
            self.view_Locator=view_Candidate()
        def search_Icon(self,Name):
            self.page.locator(self.view_Locator.searchicon_Locator()).fill(Name)
        def show_Btn(self):
             self.page.locator(self.view_Locator.showicon_Locator()).click()
        def tablename(self, verification,email):
            data = self.helperobject.json_Data()
            for column_name in data["column"]:
                col_Name = self.page.get_by_role("cell", name=column_name.strip())
                expect(col_Name).to_be_visible()
                col_inner_text=col_Name.inner_text()
                if col_inner_text=="Name":
                    name_detail = self.page.get_by_text(data["form_Alldetails"]["firstname"]).nth(1)
                    expect(name_detail).to_contain_text(verification)
                elif col_inner_text =="Email":
                     email_detail = self.page.locator(self.view_Locator.columnlocator_Email(data["form_Alldetails"]["email"]))
                     expect(email_detail).to_contain_text(email)
                elif col_inner_text == "Position":
                     position=self.page.get_by_role("cell", name="Software develpoer").first
                     self.helperobject.checkvisible(position)
                elif col_inner_text == "Status":
                     status = self.page.get_by_role("cell", name="Applied").first
                     self.helperobject.checkvisible(status)
                else:
                     qualification = self.page.get_by_role("cell", name="BE / B.Tech - Bachelor of").first
                     expect(qualification).to_be_visible()
        def edit_Icon(self):
            self.page.locator(self.view_Locator.edit_Locator()).nth(0).click()

                     
             


















            # page.locator("app-view-candidate div").filter(has_text="Name Email Position Status").nth(2)

            # email_table=self.page.get_by_text(data['form_Alldetails']["email"]).first
            # expect(email_table).to_contain_text(verification)
            
        # def full_Tableverification(self, name_Table):
        #     data1 = self.helperobject.json_Data()

        #     for i in range(0, 5):
        #         name_column = self.page.locator("app-view-candidate div").filter(has_text="Name").nth(i)
        #         if name_column.inner_text() == "Name":
        #             expect(name_Table).to_contain_text(data1["form_Alldetails"]["firstname"])

        # def full_Tableverification(self):
        #     data1 = self.helperobject.json_Data()
        #     self.page.locator("app-view-candidate div").filter(has_text="Name Email Position Status").nth(2)
        #     for i in range(0, 5):
        #             name_column = self.page.locator("app-view-candidate div").filter(has_text="Name").nth(i)
        #             if name_column.inner_text() == "Name":
        #                 expect(name_column).to_contain_text(data1["form_Alldetails"]["firstname"])
        # def columnn(self,verification,column_Name):
        #     col_Name=self.page.get_by_role("cell", name="f{column_Name}")
        #     expect(col_Name).to_be_visible()
        #     data1 =self.helperobject.json_Data()
        #     name_Table=self.page.get_by_text(data1["form_Alldetails"]["firstname"]).nth(1)
        #     expect(name_Table).to_contain_text(verification)


                  
             
      

              
        