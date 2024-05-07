class feedbacklocator:
    def written_Locator(self,type):
        return f'//li[@class="adjustList menubuttons"]//child::span[text()="{type}"]'
    def marks_Locator(self):
        return '//input[@placeholder="Marks"]'
    def add_Locator(self):
        return '//button[text()=" Add "]'
    def feedbackshow_Locator(self):
        return '//div[@id="feedback"]'
    