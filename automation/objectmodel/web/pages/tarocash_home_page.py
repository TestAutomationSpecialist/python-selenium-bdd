from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class TarocashHomePage:
    def __init__(self):
        pass

    video_title_link = Element(By.LINK_TEXT, 'Introducing Autumn 2020: One For The Ages')
    video_frame = Element(By.CSS_SELECTOR, 'div.vid-box>iframe')

    def click_video_title(self):
        self.video_frame.goto_frame()
        self.video_title_link.click()
