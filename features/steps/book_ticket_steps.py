from behave import *
from automation.objectmodel.web.pages.book_hotel_page import BookHotelPage
from automation.objectmodel.web.pages.booking_confirmation_page import BookingConfirmationPage
from automation.objectmodel.web.pages.search_hotel_page import SearchHotelPage
from automation.objectmodel.web.pages.select_hotel_page import SelectHotelPage


@given(u'I am logged in to the hotel booking site')
def step_impl(context):
    context.execute_steps(u'''given I am on the home page''')
    context.execute_steps(u'''when I enter the credentials "hiamal007" and "test"''')


@when(u'I book a ticket')
def step_impl(context):
    SearchHotelPage().search_hotel('Sydney', 'Hotel Sunshine', 'Double', '1 - One', '29/03/2020', '30/03/2020', '2 - Two', '3 - Three')
    SelectHotelPage().select_hotel(1)
    BookHotelPage().book_hotel('amal', 'raj', '23 Melb St', '7838272827291918', 'VISA', 'January', '2022', '123')


@then(u'I get a booking reference number')
def step_impl(context):
    order_reference = BookingConfirmationPage().order_reference
    print(order_reference)
    assert order_reference != ''


