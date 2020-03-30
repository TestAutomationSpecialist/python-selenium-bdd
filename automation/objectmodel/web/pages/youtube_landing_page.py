from selenium.webdriver.common.by import By

from automation.framework.web.browser import Browser
from automation.framework.web.element import Element


class YoutubeLandingPage:
    def __init__(self):
        pass

    youtube_sign_in_link = Element(By.XPATH, '//yt-formatted-string[text()="Sign in"]')

    def click_sign_in(self):
        Browser.new_window()
        self.youtube_sign_in_link.click()
