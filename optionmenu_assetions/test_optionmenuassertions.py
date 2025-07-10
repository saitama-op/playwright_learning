from playwright.sync_api import Page, expect

def test_checkbox_assertions(page: Page) -> None:
    page.goto("https://bootswatch.com/default/")

    opton_menu = page.get_by_label("Example select")
    expect(opton_menu).to_have_value("1")

    multi_option_menu = page.get_by_label("Example multiple select")
    expect(multi_option_menu).to_have_values([])
    multi_option_menu.select_option(["2", "4"])
    expect(multi_option_menu).to_have_values(["2", "4"])