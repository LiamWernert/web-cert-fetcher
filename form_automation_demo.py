from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        page.goto("https://en.wikipedia.org/w/index.php?title=Special:CreateAccount", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("Page loaded!")
        
        fields = [
            ("#wpName2", "DemoUser123"),
            ("#wpPassword2", "DemoPassword123"),
            ("#wpRetype", "DemoPassword123")
        ]

        for selector, value in fields:
            page.locator(selector).fill(value)

        page.screenshot(path="./screenshots/form_filled.png", full_page=True)
        print("Screenshot saved as form_filled.png")

        edits = page.locator(".icon-edits").inner_text().splitlines()[0]
        print(f"There have been a total of {edits} edits on Wikipedia!")

        page.close()
        browser.close()

if __name__ == "__main__":
    main()