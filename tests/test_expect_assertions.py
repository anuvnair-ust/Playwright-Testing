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

from playwright.sync_api import expect

def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login", wait_until="domcontentloaded")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
