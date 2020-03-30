from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class LoginPage:
    def __init__(self):
        pass

    username_text = Element(By.ID, 'username')
    password_text = Element(By.ID, 'password')
    login_button = Element(By.ID, 'login')
    username_error_label = Element(By.ID, 'username_span')
    password_error_label = Element(By.ID, 'password_span')
    invalid_login_details_error_label = Element(By.XPATH, '//b')

    def login(self, username, password):
        self.username_text.text = username
        self.password_text.text = password
        self.login_button.click()

    @property
    def invalid_login_error_message(self):
        return self.invalid_login_details_error_label.text
