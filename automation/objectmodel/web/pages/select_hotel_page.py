from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class SelectHotelPage:
    def __init__(self):
        pass

    select_hotel_table = Element(By.XPATH, '//form[@id="select_form"]/table//table')
    continue_button = Element(By.ID, 'continue')

    def select_hotel(self, index):
        cell = self.select_hotel_table.rows[index+1].find_element(By.XPATH, '//td')
        cell.find_element(By.XPATH, '//input').click()
        self.continue_button.click()
