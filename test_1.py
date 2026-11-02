from playwright.sync_api import expect

def test_homepage(page):
    page.goto("https://www.amazon.in")
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")