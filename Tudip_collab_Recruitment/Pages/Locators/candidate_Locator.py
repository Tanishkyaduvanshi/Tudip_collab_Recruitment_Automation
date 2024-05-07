class candidate_Locator:
    def __init__(self):
        pass
    def msg(self):
        return '//*[contains(text(), "Logged in")]'
    def candidatebtn(self):
        return '//button[@id="candidate"]'
    def detail_Locator(self,type):
        return(f'//input[@id="{type}"]')
    def dropdown_Locator(self):
        return ('//select[@id="course"]')
    def subject_Locator(self):
        return('//div[@class="filterFields col-xs-6px"]/descendant::select[@formcontrolname="subjects"]')
    def position_Locator(self):
        return('//select[@formcontrolname="position"]')
    def experience_Locator(self):
        return('//select[@formcontrolname="experience"]')
    def calander_Icon_locator(self):
        return ('//span[@class="p-button-icon pi pi-calendar"]')
    def calander_Textarea_locator(self):
        return ('//*[@formcontrolname="dob"]/descendant::input[@type="text"]')
    def active_Locator(self):
        return('//select[@formcontrolname="status"]')
    def remuse_Locator(self):
        return ('//input[@type="file"]')
    def submitbtn(self):
        return '//button[@class="btn btn-primary margintop add-item-icon ion-checkmark-circled btn btn-md pull-right alignForMobile" and text()=" Submit"]'
    def iconperson_Locator(self):
        return ('//a[@class="al-sidebar-list-link ng-star-inserted"]/child::i[@class="icon ion-person-add ng-star-inserted"]')
    def profile_ICon (self):
        return ('//a[@id="user-profile-dd"]')
    def signout_Locator(self):
        return ('//*[text()="Sign out"]')