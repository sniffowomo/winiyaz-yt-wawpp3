# -- Imports ---
from playwright.sync_api import sync_playwright, Error
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting
from src.ban import banner2

# --- User Agent and Websites ---
urls = [
    "https://www.coingecko.com/",
    "https://www.femscat.com/main.php",
    "https://www.meanbitches.com/",
    "https://www.1.com",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def func11():
    with sync_playwright() as p:
        rprint("[blue1][OK] Starting Playwright Script...[/blue1]")

        for url in urls:
            banner2(f"Testing - {url}")
            # Launching Browser and Navigating
            rprint("[blue1][OK] Launching Broswer...[/blue1]")
            browser = p.chromium.launch()
            page = browser.new_page(user_agent=uA)

            try:
                # Opening New Page
                page.goto(url, timeout=0)
                rez = page.goto(url, timeout=0)
                rezStatus = rez.status
                if rezStatus == 200:
                    rprint(f"[green3][OK] Go to page - {url} - {rezStatus}[/green3]")
                else:
                    rprint(f"[red3][FAIL] Go to page - {url} - {rezStatus}[/red3]")

                # Actions on Page
                rprint(f"[green3][OK] Grab Title - {url}[/green3]")
                rprint(page.title())

            except Error as e:
                rprint(f"[red3][FAIL] Error navigating to {url}: {e}[/red3]")

            finally:
                # Closing Browser
                rprint("[gold3][OK] Shutdown Browser[/gold3]")
                browser.close()


if __name__ == "__main__":
    func11()
