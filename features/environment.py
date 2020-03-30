from automation.framework.web.browser import Browser
from behave import fixture


def before_scenario(context, scenario):
    if 'web' in context.tags:
        Browser.initialise_driver()
        context.browser = Browser.driver


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
        Browser.driver = None
        Browser.last_window_handles

