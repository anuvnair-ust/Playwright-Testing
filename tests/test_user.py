from playwright.sync_api import Page, expect
import time 
def test_user_name(user_data):
    assert user_data["username"] == "testuser"

def test_username():
    username = "admin"
    assert username == "admin"

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


from playwright.sync_api import expect
def test_click_button(page):
    page.goto("https://www.playwrightautomation.com/practice.html")
    button = page.get_by_role(
        "button",
        name="Submit"
    )
    expect(button).to_be_visible()
    button.click()


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

# from playwright.sync_api import expect
# def test_search_product(page):
#     page.goto("https://www.amazon.com")
#     search_box = page.get_by_role(
#         "searchbox",
#         name = "Search Amazon"
#     )
#     search_box.fill("headphones")
#     search_box.press("Enter")
#     expect(page).to_have_url("https://www.amazon.com/s?k=headphones&ref=nb_sb_noss")


# -------------------------------------------------------------------------------------------------------------
# TEXT EXTRACTION
# -------------------------------------------------------------------------------------------------------------

# inner_text() - Returns the rendered text of an element

def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h1").inner_text()
    print("Heading:",heading)
    assert heading == "Welcome to the-internet"


# text_content() - Returns the text content of a DOM element, including text that may not be visible

def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h2")
    print("Heading:",heading)
    expect(heading).to_have_text("Available Examples")



# all_text_contents() - Useful when you want the text from multiple matching elements

def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    links = page.locator("ul li a").all_text_contents()
    print(links)
    assert len(links) > 0


# get_attribute(href) - Read an element attribute

def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/", wait_until="domcontentloaded")
    href = page.get_by_role("link", name="Subdirectories").get_attribute("href")
    print(href)

# ---------------------------------------------------------------------------------------------------------------------------------
# Expect assertions in Playwright
# ---------------------------------------------------------------------------------------------------------------------------------

# Common assertion

# to be visible() - Element is visible
# to be hidden() - Element is hidden
# to_have_text() - Exact text or expected test list
# to_contain_text() - Text contains a particular value
# to_be_enabled() - Element is enabled

# How Test Works

# 1.Opens the login page
# 2.Enters the documented username and password
# 3.Click the Login Button
# Verifies the browser navigated to the secure page
# Verifies success message
# Confirm the Secure Area heading is visible

def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login", wait_until="domcontentloaded")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()


# ------------------------------------------------------------------------------------------------------------------------------
# PLAYWRIGHT WAITING MECHANISM
# --------------------------------------------------------------------------------------------------

# Auto-Waiting









def test_zoom_meeting_registration(page: Page):
    page.goto("https://ust.zoom.us/meeting/register/wROkcnzOSO2Z7jeg-vMTPA#/registration")
    page.get_by_label("First Name").fill("Anu")
    page.get_by_label("Last Name").fill("V Nair")
    page.get_by_label("Email Address").fill("anu.vnair@ust.com")
    page.get_by_label("UST UID").fill("314087")
    expect(page.get_by_label("First Name")).to_have_value("Anu")
    expect(page.get_by_label("Last Name")).to_have_value("V Nair")
    expect(page.get_by_label("Email Address")).to_have_value("anu.vnair@ust.com")
    expect(page.get_by_label("UST UID")).to_have_value("314087")

    register_button = page.get_by_role("button",name="Register and Join")
    expect(register_button).to_be_visible()


def test_native_dropdown(page):
    page.goto("https://practice.expandtesting.com/dropdown")

    dropdown = page.locator("#dropdown")

    expect(dropdown).to_be_visible()

    dropdown.select_option("1")

    dropdown.select_option("2")

    expect(dropdown).to_have_value("2")

    print("Dropdown options were selected successfully")


def test_checkboxes(page : Page):
    page.goto("https://practice.expandtesting.com/checkboxes",
              wait_until="domcontentloaded",
              timeout=15000)

    checkboxes = page.locator("input[type='checkbox']")
    first_checkbox = checkboxes.nth(0)
    second_checkbox = checkboxes.nth(1)

    expect(first_checkbox).to_be_visible()
    expect(second_checkbox).to_be_visible()

    first_checkbox.check()
    expect(first_checkbox).to_be_checked()

    expect(second_checkbox).to_be_checked()
    
    first_checkbox.uncheck()
    expect(first_checkbox).not_to_be_checked()
    expect(second_checkbox).to_be_checked()
    
    print("Checkbox selection and deselection tests passed")


def test_radio_button(page):

    page.goto("https://practice.expandtesting.com/radio-buttons")

    blue_radio = page.get_by_label("Blue")
    red_radio = page.get_by_label("Red")
    yellow_radio = page.get_by_label("Yellow")

    blue_radio.check()
    expect(blue_radio).to_be_checked()
    
    red_radio.check()
    expect(red_radio).to_be_checked()


    yellow_radio.check()
    expect(yellow_radio).to_be_checked()
    expect(blue_radio).not_to_be_checked()
    expect(red_radio).not_to_be_checked()
    print("\nRadio button selection tests passed")

# Advanced Browser Interactions

def test_multiple_tabs(page: Page):
    page.goto("https://www.example.com")
    expect(page).to_have_title("Example Domain")

    second_page = page.context.new_page()
    second_page.goto("https://www.wikipedia.org")
    expect(second_page).to_have_title("Wikipedia")

    expect(page).to_have_title("Example Domain")

    all_pages = page.context.pages
    assert len(all_pages) == 2
    print("No of open pages:", len(all_pages))
    expect(
        second_page.get_by_role("heading", name="Wikipedia")).to_be_visible()
    second_page.close()

    expect(page).to_have_title("Example Domain")
    assert len(page.context.pages) == 1
    print("Multiple tabs test passes successfully")


from playwright.sync_api import Page, expect
def test_multiple_tabs(page: Page):
    #step 1: open first website
    page.goto("https://example.com")
    #Verify the first webpage
    expect(page).to_have_title("Example Domain")
    print("First tab URL: ", page.url)
    #Step 2: Create a second tab in same browser
    second_page = page.context.new_page()
    second_page.goto("https://www.wikipedia.org")
    #Verify the second website
    expect(second_page).to_have_title("Wikipedia")
    print("Second tab URL:", second_page.url)
    #Step 3: Verify the original tab is still open
    expect(page).to_have_title("Example Domain")
    #Step 4: Verify that two pages exist in the context
    all_pages = page.context.pages
    assert len(all_pages) == 2
    print("No.of open pages:", len(all_pages))
    # Step5: Interact with the second tab     
    expect(second_page.get_by_role("heading", name="Wikipedia")).to_be_visible()
    # Step 6: Close the second tab
    second_page.close()
    # Step 7: Verify the original tab remains open
    expect(page).to_have_title("Example Domain")
    assert len(page.context.pages) == 1
    print("Multiple tabs test passes successfully")


# Handling a New Tab Opened by Clicking a link

# Open the original web

from pathlib import Path

from playwright.sync_api import expect


def test_new_tab_from_link(page):
    # Step 1: Open the local HTML page
    html_file = Path(__file__).with_name("open_new_tab.html")
    page.goto(html_file.resolve().as_uri())

    # Step 2: Verify the original page
    expect(page.get_by_role("heading", name="Original Page")).to_be_visible()

    # Step 3: Verify the link exists
    link = page.get_by_role("link", name="Open Example Website in a New Tab")
    expect(link).to_be_visible()

    # Step 4: Click the link and capture the new tab
    with page.context.expect_page() as new_page_info:
        link.click()
    new_page = new_page_info.value

    # Step 5: Wait for the new tab to finish loading
    new_page.wait_for_load_state("domcontentloaded")

    # Step 6: Verify the new tab URL
    expect(new_page).to_have_url("https://example.com/")
    print("Original tab URL:", page.url)
    print("New tab URL:", new_page.url)

    # Step 7: Close the new tab
    new_page.close()
    print("New Tab test passed successfully.")

# ---------------------------------------------------------------
# PLAYWRIGHT ADVANCED TOPICS
# ------------------------------------------------------------------

# Parallel Execution
# Run multiple tests simultaneously to reduce execution time.

