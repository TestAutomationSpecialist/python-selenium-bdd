from behave import *
from automation.objectmodel.web.pages.login_page import LoginPage
from automation.objectmodel.web.pages.search_hotel_page import SearchHotelPage


@given('I am on the home page')
def home_page(context):
    context.browser.get("http://www.adactin.com/HotelApp/index.php")


@when('I enter the credentials "{username}" and "{password}"')
def enter_username_and_password(context, username, password):
    context.username = username
    LoginPage().login(username, password)


@then('I am able to login successfully')
def verify_successful_login(context):
    print(SearchHotelPage().user_greeting)
    assert (SearchHotelPage().user_greeting == f'Hello {context.username}!')


@then('I am not able to login successfully')
def verify_successful_login(context):
    print(LoginPage().invalid_login_error_message)
    assert ('Invalid Login details or Your Password might have expired. ' in LoginPage().invalid_login_error_message)

