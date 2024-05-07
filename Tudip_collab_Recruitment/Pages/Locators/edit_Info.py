class edit_Info:
    def __init__(self):
        pass
    def edit_namelocator(self):
        return ('//input[@id="name"]')
    def edit_Submit(self):
        return ('//button[@type="submit" and text()=" Submit "]')
    def popup_message(self):
        return ('//*[contains(text(), "Candidate updated successfully")]')
    def searcheditname_Locator(self):
        return ('//input[@id="searchInput"]')
    def showbtn(self):
        return('//button[text()=" Show "]')
    def feedback_Locator(self):
        return('//td[@class="ng2-smart-actions ng-star-inserted"]//descendant::i[@class="fa fa-pencil-square-o"]')

    