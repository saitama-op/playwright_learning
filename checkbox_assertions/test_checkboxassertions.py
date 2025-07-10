from playwright.sync_api import Page, expect

def test_checkbox_assertions(page: Page) -> None:
    page.goto("https://bootswatch.com/default/")
    default_checkbox = page.get_by_label("Default checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    # Default checkbox should be unchecked
    expect(default_checkbox).not_to_be_checked()
    # Checked checkbox should be checked
    expect(checked_checkbox).to_be_checked()
  
