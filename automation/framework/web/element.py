from datetime import time
from select import select

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from automation.framework.web.browser import Browser


class Element:
    def __init__(self, locator_type, locator_value=None):
        self.retry_count = 0
        self.locator_type = locator_type
        self.locator_value = locator_value

    @property
    def element(self):
        # Add code to handle any overlays that needs to go before finding the element
        return Browser.driver.find_element(self.locator_type, self.locator_value)

    @element.setter
    def element(self, value):
        self.element = value

    def handle_exceptions(self, function, args=None):
        try:
            if args is None:
                return function
            else:
                return function(args)
        except StaleElementReferenceException:
            # Add more exceptions if they need to be handled
            if self.retry_count < 6:
                return function(args)
                print('Retried function {function} {self.retry_count} times')
                self.retry_count = self.retry_count + 1
                time.sleep(.500)
            else:
                raise StaleElementReferenceException

    def click(self):
        self.handle_exceptions(self.element.click())

    @property
    def text(self):
        if self.element.tag_name == 'select':
            return self.handle_exceptions(Select(self.element).first_selected_option().text)
        else:
            return self.handle_exceptions(self.element.text)

    @text.setter
    def text(self, text):
        if self.element.tag_name == 'select':
            self.handle_exceptions(Select(self.element).select_by_visible_text(text))
        else:
            self.handle_exceptions(self.element.clear())
            self.handle_exceptions(self.element.send_keys(text))

    def attribute(self, attribute_name):
        return self.handle_exceptions(self.element.get_attribute(attribute_name))

    def goto_frame(self, switch_first_to_default=None):
        if switch_first_to_default is not None:
            self.handle_exceptions(Browser.driver.switch_to_default_content())
        self.handle_exceptions(Browser.driver.switch_to.frame(self.element))

    @property
    def row(self):
        return self.element.find_element(By.XPATH, '//tr')

    @property
    def rows(self):
        return self.element.find_elements(By.XPATH, '//tr')

    @property
    def columns(self):
        return self.element.find_element(By.XPATH, '//td')

    @property
    def columns(self):
        return self.element.find_elements(By.XPATH, '//td')

    def column_number(self, row, text):
        for self.column in row.columns:
            if self.column.text == text:
                return self.row.columns.index(self.column)
        raise Exception(f"Unable to find row with text {text}")

    def cell(self, row_search_text, column_search_text):
        for row in self.rows:
            if row_search_text in row.text:
                for column in row.columns:
                    if column_search_text in column.text:
                        return column

        raise Exception(f"Unable to find cell with row text {row_search_text} and column text {column_search_text}")





