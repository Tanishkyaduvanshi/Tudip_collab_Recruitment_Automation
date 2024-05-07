class view_Candidate:
    def searchicon_Locator(self):
        return ('//input[@id="searchInput"]')
    def showicon_Locator(self):
        return ('//button[text()=" Show "]')
    def table_Locator(self):
        return ('//tbody[@_ngcontent-rkn-c46]/child::tr')
    # //td[count(//th[.="Name"]//preceding-sibling::th)+1]")
    def edit_Locator(self):
        return ('//i[@title="Edit candidate"]')
    def columnlocator_Email(self,type):
        return f'//div[@class="ng-star-inserted" and text()="{type}"]'
    def textverification_Column(self):
        return ''