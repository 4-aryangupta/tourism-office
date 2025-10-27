from playwright.sync_api import sync_playwright

results = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://exploremetrices.wasmer.app/", wait_until="load")

    
    headings = page.query_selector_all("h1, h2, h3")
    if headings:
        for h in headings:
            results.append(f"Heading found: {h.inner_text()}")
    else:
        results.append("No headings found")


    buttons = page.query_selector_all("button")
    if buttons:
        for i, b in enumerate(buttons, start=1):
            results.append(f"Button {i} exists: {b.inner_text()}")
    else:
        results.append("No buttons found")

    links = page.query_selector_all("a")
    if links:
        for i, l in enumerate(links, start=1):
            results.append(f"Link {i}: {l.get_attribute('href')}")
    else:
        results.append("No links found")

    input("Press Enter to close browser...")
    browser.close()


with open("full_test_report.txt", "w") as f:
    for line in results:
        f.write(line + "\n")

print("Test report saved to full_test_report.txt")
