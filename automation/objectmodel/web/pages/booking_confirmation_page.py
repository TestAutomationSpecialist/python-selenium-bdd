from selenium.webdriver.common.by import By
from automation.framework.web.element import Element
from selenium.webdriver.support import expected_conditions


class BookingConfirmationPage:

    order_number_label = Element(By.ID, 'order_no')

    @property
    def order_reference(self):
        # Explicit Wait
        #expected_conditions().presence_of_element_located(By.ID, 'order_no')
        return self.order_number_label.attribute('value')
