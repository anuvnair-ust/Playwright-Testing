from playwright.sync_api import Page, expect

def test_user_name(user_data):
    assert user_data["username"] == "testuser"

def test_username():
    username = "admin"
    assert username == "admin"

def test_values():
    assert 10 > 5
    assert "Python" in "Python Playwright"
    assert 5 != 3
    assert [1, 2, 3] == [1, 2, 3]

from playwright.sync_api import expect

import re
from playwright.sync_api import expect
def test_amazon_homepage(page):
    response = page.goto(
        "https://www.amazon.com",
        wait_until="domcontentloaded",#Browser has finished parsing the initial HTML document
        timeout=15000
    )
    print("Response status:", response.status if response else None)
    print("Page title: ",repr(page.title()))
    print("Current URL:", page.url)
    expect(page).to_have_title(
        re.compile(r"Amazon\.com")
    )


#Parameterization - Testing Multiple Inputs
#It allows one test function to run with different input 
#values 

import pytest
@pytest.mark.parametrize(
    "number, expected",
    [
        (2, 4),
        (3, 9),
        (4, 16)
    ]
)
def test_square(number, expected):
    assert number * number == expected


#Markers - Organizing tests into categories 

#Smoke test: Quick checks of essential functionality
#Regression tests: Checks that existing functionality still
#work
#Slow tests: Tests that take longer to execute.

import pytest
@pytest.mark.smoke
def test_homepage_title():
    assert "Home" == "Home"
@pytest.mark.regression
def test_user_status():
    assert "Active" == "Active"
    
#Eg: Verify a Username input 

from playwright.sync_api import expect

def test_username_input(page):
    page.goto("https://www.playwrightautomation.com/practice.html")
    name_input = page.get_by_placeholder("Enter your name")
    name_input.fill("Vikas")
    expect(name_input).to_have_value("Vikas")


def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    href = page.get_by_role("link", name="Subdirectories").get_attribute("href")
    print(href)

#Waiting Mechanism in Playwright 


#Explicit wait using locator.wait_for() 
from playwright.sync_api import expect
def test_dynamic_loading(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    heading = page.locator("#finish h4")
    expect(heading).to_have_text("Hello World!")




# -------------------------------------------------------------------------------------------------------------
# LOCATORS
# -------------------------------------------------------------------------------------------------------------

# Locator Methods:
# get_by_role() - Find elements by their accessible role and name
# get_by_label() - Find form controls by their associated label
# get_by_text() - Find elements by visible text
# get_by_placeholder() - Find inputs by placeholder text
# get_by_test_id() - Find elements by using a dedicated test ID
# locator() - Locate elements using CSS selectors and other supported selectors





# ----------------------------------------------------------------------------------------------------
# ACTIONS AND ASSERTIONS
# ----------------------------------------------------------------------------------------------------

# click() - Click an element
# fill() - Replace an input's content
# press() - Press a keyboard key
# check() - Check a chekbox or radio button
# uncheck() - Uncheck a checkbox
# select_option() - Select an option in a native HTML element
# hover() - Move the pointer over an element
# input_value() - Read the value of an input field
# text_content() - Read the text content from an element

from playwright.sync_api import expect
def test_search_product(page):
    page.goto("https://www.amazon.com")
    search_box = page.get_by_role(
        "searchbox",
        name = "Search Amazon"
    )
    search_box.fill("headphones")
    search_box.press("Enter")
    expect(page).to_have_url("https://www.amazon.com/s?k=headphones&ref=nb_sb_noss")

