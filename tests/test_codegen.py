# playwright codegen https://www.saucedemo.com/
# playwright codegen --target=java https://www.saucedemo.com/
# $env:PWDEBUG="1"; python -m pytest tests/test_codegen.py -s
# python -m pytest tests/test_codegen.py -v --tracing retain-on-failure --screenshot only-on-failure --output=test-results

from playwright.sync_api import sync_playwright, expect, Page
def test_login() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        browser.close()

def test_login_2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    # expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#Inspector - It is an interactive debugging tool that lets you inspect and control a 
#playwright test while it runs.

#TraceViewer - It is a debugging tool that lets you
#inspect a recorded test execution afte the test has
#been finished.

#End to end Testing in Playwright Python

#Reusable Functions - Write code once and use it across multiple
#tests

#Test data - Use different inputs to test the same workflow 
#API Mocking - Simulate API responses without calling actual 
#backend service

#End to End Workflow 

#A workflow is a sequence of actions that a user performs to 
#accomplish a task.

#Start ->Open LOgin Page -> Enter Username -> Enter Password ->
# Click Login -> Verify Dashboard -> End 













import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"login-credentials\"]").dblclick()
    page.locator("body").press("ControlOrMeta+c")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"login-password\"]").dblclick()
    page.locator("body").press("ControlOrMeta+c")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("o")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("k")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("9")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()

#     # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"login-credentials\"]").dblclick()
    page.locator("body").press("ControlOrMeta+c")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"login-password\"]").dblclick()
    page.locator("body").press("ControlOrMeta+c")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("o")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("k")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("9")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()


from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page, expect
def test_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    # expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")