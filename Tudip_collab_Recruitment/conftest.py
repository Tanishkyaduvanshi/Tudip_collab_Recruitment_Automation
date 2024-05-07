from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os,pytest

@pytest.fixture(scope="function")
def set():
       with sync_playwright() as p:
        load_dotenv()
        browser = p.chromium.launch(headless=eval(os.getenv('headless')))
        context = browser.new_context(record_video_dir=os.getenv("recordVideoDirpath"))
        page = context.new_page()

       #  Total_page=page.context.pages
       #  new_page=Total_page[1]
       #  new_page.bring_to_front()

       #  Total_page=page.context.pages
       #  second_page=Total_page[2]
       #  second_page.bring_to_front()

        yield page
        page.close()