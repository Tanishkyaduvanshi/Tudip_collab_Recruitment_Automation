import sys
sys.path.append('/home/tanishkyadav/Git_folder/tanishk-yadav/Tudip_collab_Recruitment')
from playwright.sync_api import sync_playwright,Page,expect
import json

class helper:
    def checkvisible(self, text):
        expect(text).to_be_visible()
    def notempty(self,text):
        expect(text).not_to_be_empty()

    def json_Data(self):  # Add 'self' as the first parameter
        with open('config.json') as file:
            data = json.load(file)
        return data

