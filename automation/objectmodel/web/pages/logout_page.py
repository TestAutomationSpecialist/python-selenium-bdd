from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class SearchHotelPage:
    def __init__(self):
        pass

    logout_link = Element(By.LINK_TEXT, 'Logout')

    def logout(self):
        self.logout_link.click()
