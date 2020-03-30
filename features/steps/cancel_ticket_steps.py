from behave import *
from automation.objectmodel.web.pages.booking_confirmation_page import BookingConfirmationPage
from automation.objectmodel.web.pages.itinerary_page import ItineraryPage


@given(u'I have a booking reference number')
def step_impl(context):
    context.execute_steps(u'''given I am logged in to the hotel booking site''')
    context.execute_steps(u'''when I book a ticket''')
    context.booking_reference = BookingConfirmationPage().order_reference


@when(u'I cancel the booking')
def step_impl(context):
    itinerary_page = ItineraryPage()
    itinerary_page.goto_itinerary()
    itinerary_page.cancel_booking(context.booking_reference)


@then(u'the cancelled ticket does not appear in the itinerary page')
def step_impl(context):
    assert context.booking_reference not in ItineraryPage().booking_references
