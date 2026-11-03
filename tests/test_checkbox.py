from playwright.sync_api import Page, expect
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