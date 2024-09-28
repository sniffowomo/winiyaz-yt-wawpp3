# -- Imports ---
from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting
import os

# --- User Agent and Websites ---
URLS = [
    "https://www.coingecko.com/",
    "https://www.femscat.com/main.php",
    "https://www.meanbitches.com/",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def func2():
    with sync_playwright() as p:
        rprint("[blue1][OK] Starting Playwright Script...[/blue1]")

        # Launching Browser and Navigating
        rprint("[blue1][OK] Launching Broswer...[/blue1]")
        browser = p.chromium.launch()
        page = browser.new_page(user_agent=uA)

        # Recording video
        # Rectording Viedo ACtions
        rprint("[orange1][OK] StartRecording...[/orange1]")
        context_config = {
            "record_video_dir": "clicks/",
            "record_video_size": {"width": 640, "height": 480},
            "user_agent": uA,
            "locale": "de-DE",
            "timezone_id": "Europe/Berlin",
        }
        context = browser.new_context(**context_config)
        page = context.new_page()

        # Opening New Page
        page.goto(URLS[0], timeout=0)

        # Define the url here the array is being accessed from the variable URLS
        rez = page.goto(URLS[0], timeout=0)
        rezStatus = rez.status
        rprint(f"[green3][OK] Go to page - {URLS[0]} - {rezStatus}[/green3]")

        #  Actions on Page
        rprint(f"[green3][OK] Grab Title - {URLS[0]}[/green3]")
        rprint(page.title())

        # Further Actions on page
        # Locate element called Cryptocurrencies and do a sublick
        rprint("[orange1][OK] LickingPussy....[/orange1]")
        # page.set_default_timeout(200)
        page.click(
            'div.nav-label.dark\\:\\!tw-text-moon-50.tw-text-gray-700.dark\\:tw-text-moon-100.tw-font-semibold.tw-text-sm.tw-leading-5 >> text="Cryptocurrencies"'
        )
        page.click(
            'a.dark\\:tw-text-moon-100.dark\\:hover\\:tw-bg-moon-700.dark\\:hover\\:tw-text-moon-50.hover\\:tw-bg-gray-100.hover\\:tw-text-gray-900.tw-flex.tw-items-center.tw-py-3.tw-px-2.tw-rounded-lg.tw-font-semibold.tw-text-gray-700.tw-text-sm >> text="By Market Cap"'
        )

        # Create sreenshot - wih current date time
        page.screenshot(path=f"clicks/{c_d}-s1.png", full_page=True)

        # Closing Browser
        rprint("[gold3][OK] Shutdown Browser[/gold3]")
        browser.close()

        # View new files in directory
        rprint("[blue1][OK] View new files in directory...[/blue1]")
        os.system("ls -alh clicks")
