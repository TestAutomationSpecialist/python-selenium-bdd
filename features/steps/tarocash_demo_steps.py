from behave import *
from automation.framework.web.browser import Browser
from automation.objectmodel.web.pages.tarocash_home_page import TarocashHomePage
from automation.objectmodel.web.pages.youtube_landing_page import YoutubeLandingPage


@given(u'I am on the Tarocash home page')
def step_impl(context):
    context.browser.get("https://www.tarocash.com.au/au/")


@when(u'I click on the title of the embedded video')
def step_impl(context):
    TarocashHomePage().click_video_title()


@when(u'I click on the youtube logo in the youtube page')
def step_impl(context):
    YoutubeLandingPage().click_sign_in()


@then(u'I am taken to the youtube home page')
def step_impl(context):
    print(context.browser.title)
    assert context.browser.title == 'YouTube'
