# -------------------------------------------------------------------------------------------------------------
# TEXT EXTRACTION
# -------------------------------------------------------------------------------------------------------------

# inner_text() - Returns the rendered text of an element

from playwright.sync_api import expect

def test_extract_heading_inner_text(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h1").inner_text()
    print("Heading:",heading)
    assert heading == "Welcome to the-internet"


# text_content() - Returns the text content of a DOM element, including text that may not be visible
def test_extract_heading_text_content(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h2").text_content()
    print(heading)



# expect(locator).to_have_text() - Auto-retrying assertion that the element's text matches the expected value

def test_extract_heading_expect(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h2")
    print("Heading:",heading)
    expect(heading).to_have_text("Available Examples")



# all_text_contents() - Useful when you want the text from multiple matching elements

def test_heading_all_text_content(page):
    page.goto("https://the-internet.herokuapp.com/")
    links = page.locator("ul li a").all_text_contents()
    print(links)
    assert len(links) > 0


# get_attribute(href) - Read an element attribute

def test_heading_get_attribute(page):
    page.goto("https://the-internet.herokuapp.com/", wait_until="domcontentloaded")
    href = page.get_by_role("link", name="Subdirectories").get_attribute("href")
    print(href)

