from selenium.webdriver.common.by import By
from automation.framework.web.browser import Browser
from automation.framework.web.element import Element


class ItineraryPage:
    def __init__(self):
        pass

    booked_itinerary_link = Element(By.LINK_TEXT, 'Booked Itinerary')
    booked_itinerary_table = Element(By.XPATH, '//form[@id="booked_form"]/table//tr[2]//table')
    cancel_selected_button = Element(By.NAME, 'cancelall')

    def goto_itinerary(self):
        self.booked_itinerary_link.click()

    def cancel_booking(self, booking_reference):
        all_cancel_buttons = Browser.driver.find_elements(By.XPATH, '//td[3]/input')
        for cancel_button in all_cancel_buttons:
            cancel_cell_value = cancel_button.get_attribute('value')
            if cancel_cell_value is not None and booking_reference in cancel_cell_value:
                cancel_button.click()
                break
            if cancel_button == all_cancel_buttons[-1]:
                raise Exception(f'Unable to find row with booking ref {booking_reference}')
        Browser.accept_alert(booking_reference)

    @property
    def booking_references(self):
        booking_reference_ids = []
        for row in self.booked_itinerary_table.rows:
            booking_reference_cell = row.find_element(By.XPATH, '//td[3]/input')
            booking_reference_ids.append(booking_reference_cell.get_attribute('value'))
        return booking_reference_ids
