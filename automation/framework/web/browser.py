from selenium import webdriver


class Browser:
    driver = None
    last_window_handles = None

    @staticmethod
    def initialise_driver():
        if Browser.driver is None:
            Browser.driver = webdriver.Chrome()
            Browser.driver.implicitly_wait(5)
            Browser.last_window_handles = []

    @staticmethod
    def new_window():
        Browser.last_window_handles.append(Browser.driver.current_window_handle)
        Browser.driver.switch_to.window(Browser.driver.window_handles[-1])

    @staticmethod
    def last_window():
        Browser.driver.switch_to.window(Browser.last_window_handles[-1])
        Browser.last_window_handles.pop()

    @staticmethod
    def accept_alert(text=''):
        alert = Browser.driver.switch_to.alert
        alert_text = alert.text
        if text in alert_text:
            alert.accept()
        else:
            raise Exception(f'Invalid alert with text {alert_text} and not containing {text}')
        return alert_text

    @staticmethod
    def dismiss_alert(text):
        alert = Browser.driver.switch_to.alert()
        alert_text = alert.text
        if text in alert_text:
            alert.dismiss()
        else:
            raise Exception(f'Invalid alert with text {alert_text} and not containing {text}')
        return alert_text


