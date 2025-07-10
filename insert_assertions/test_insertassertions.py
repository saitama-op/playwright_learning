from playwright.sync_api import Page, expect

def test_get_started_link(page: Page) -> None:
    page.goto("https://playwright.dev/python")
    expect(page.get_by_role("link", name="Get started")).to_be_visible()
    input = page.get_by_placeholder("Search docs")

    #input is hidden before button click
    expect(input).to_be_hidden()

    # search button
    search_btn=page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK")

    #popup should be editable and empty
    expect(input).to_be_editable()

    # input should be empty
    expect(input).to_be_empty()

    #type some query in the input
    query = "assertions"
    input.fill(query)
    expect(input).to_have_value(query)