from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class SearchHotelPage:
    def __init__(self):
        pass

    user_greeting_label = Element(By.ID, 'user'
                                         'name_show')
    location_select = Element(By.ID, 'location')
    hotel_select = Element(By.ID, 'hotels')
    room_type_select = Element(By.ID, 'room_type')
    number_of_rooms_select = Element(By.ID, 'room_nos')
    check_in_date_text = Element(By.ID, 'datepick_in')
    check_out_date_text = Element(By.ID, 'datepick_out')
    adults_per_room_select = Element(By.ID, 'adult_room')
    children_per_room_select = Element(By.ID, 'child_room')
    search_button = Element(By.ID, 'Submit')

    def search_hotel(self, location, hotel, room_type, number_of_rooms, from_date, to_date, adult_per_room, child_per_room):
        self.location_select.text = location
        self.hotel_select.text = hotel
        self.room_type_select.text = room_type
        self.number_of_rooms_select.text = number_of_rooms
        self.check_in_date_text.text = from_date
        self.check_out_date_text.text = to_date
        self.adults_per_room_select.text = adult_per_room
        self.children_per_room_select.text = child_per_room
        self.search_button.click()

    @property
    def user_greeting(self):
        return self.user_greeting_label.attribute('value')
