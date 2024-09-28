# py3.py - Next tytorial overview

# -- Imports ---
from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting
import os

# --- User Agent and Websites ---
URLS = [
    "https://www.coingecko.com/",
    "https://megasite.meanworld.com/",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def func5():
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
        page.goto(URLS[1], timeout=0)

        # Define the url here the array is being accessed from the variable URLS
        rez = page.goto(URLS[1], timeout=0)
        rezStatus = rez.status
        rprint(f"[green3][OK] Go to page - {URLS[1]} - {rezStatus}[/green3]")

        #  Actions on Page
        rprint(f"[green3][OK] Grab Title - {URLS[1]}[/green3]")
        rprint(page.title())

        # Further Actions on page
        # Locate element called Cryptocurrencies and do a sublick
        rprint("[orange1][OK] LickingPussy....[/orange1]")
        # Ente Site
        link = page.locator('a[href="#enter"].btn-enter.s_enter')
        link.click()
        # Go to Categories
        rprint("[orange1][OK] LickingPussy.... GoTo-Categories[/orange1]")
        link = page.get_by_role("link", name="Categories")
        link.click()
        rprint(f"[yellow2][OK] url = {page.url}  [/yellow2]")
        # Go to Armpits Category
        rprint("[orange1][OK] LickingPussy.... GoTo-Armpits[/orange1]")
        link = page.locator('a[href="#enter"].btn-enter.s_enter')
        link = page.get_by_role("link", name="Armpit")
        link.click()
        page.wait_for_load_state("networkidle")
        rprint(f"[yellow2][OK] url = {page.url}  [/yellow2]")
        # Go TO Bella
        link = page.locator(
            'a[href="https://megasite.meanworld.com/updates/Bad-Bella-Slave-Orders.html"] img[alt="2304_badbella_slaveorders"]'
        )
        link.click()
        page.wait_for_load_state("networkidle")
        rprint(f"[yellow2][OK] url = {page.url}  [/yellow2]")
        # Open Video
        link = page.locator(
            'a[onclick="tload(\'/trailers/badbella_slaveorders_tr.mp4\', this)"] img[src="images/play.png"]'
        )
        link.click()
        page.wait_for_load_state("networkidle")
        rprint(f"[yellow2][OK] url = {page.url}  [/yellow2]")

        # Create sreenshot - wih current date time
        page.screenshot(path=f"clicks/{c_d}-s1.png", full_page=True)

        # Closing Browser
        rprint("[gold3][OK] Shutdown Browser[/gold3]")
        browser.close()

        # View new files in directory
        rprint("[blue1][OK] View new files in directory...[/blue1]")
        os.system("ls -alh clicks")
