# More testing with the progress bar at each operation

import time
import os
from rich.progress import Progress
from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting

# --- User Agent and Websites ---
urls = [
    "https://www.coingecko.com/",
    "https://www.femscat.com/main.php",
    "https://www.meanbitches.com/",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def func24():
    with sync_playwright() as p:
        rprint("[blue1][OK] Starting Playwright Script...[/blue1]")

        # Launching Browser and Navigating
        rprint("[blue1][OK] Launching Broswer...[/blue1]")
        start_time = time.time()
        browser = p.chromium.launch()
        page = browser.new_page(user_agent=uA)
        rprint(
            f"[green3][OK] Browser launched in {time.time() - start_time:.2f} seconds[/green3]"
        )

        # Opening New Page
        rprint(f"[green3][OK] Go to page - {urls[0]}[/green3]")
        start_time = time.time()
        with Progress() as progress:
            task = progress.add_task("[cyan]Loading page...", total=100)
            page.goto(urls[0], timeout=0)
            rez = page.goto(urls[0], timeout=0)
            rezStatus = rez.status
            rprint(f"[green3][OK] Go to page - {urls[0]} - {rezStatus}[/green3]")
            progress.update(task, completed=100)
        rprint(
            f"[green3][OK] Page loaded in {time.time() - start_time:.2f} seconds[/green3]"
        )

        # Grab Title
        rprint(f"[green3][OK] Grab Title - {urls[0]}[/green3]")
        start_time = time.time()
        with Progress() as progress:
            task = progress.add_task("[cyan]Grabbing title...", total=100)
            title = page.title()
            rprint(title)
            progress.update(task, completed=100)
        rprint(
            f"[green3][OK] Title grabbed in {time.time() - start_time:.2f} seconds[/green3]"
        )

        # Create screenshot - with current date time
        rprint(f"[green3][OK] Create screenshot - {c_d}-s1.png[/green3]")
        start_time = time.time()
        with Progress() as progress:
            task = progress.add_task("[cyan]Creating screenshot...", total=100)
            page.screenshot(path=f"clicks/{c_d}-s1.png", full_page=True)
            progress.update(task, completed=100)
        rprint(
            f"[green3][OK] Screenshot created in {time.time() - start_time:.2f} seconds[/green3]"
        )
        os.system("ls -al clicks/")

        # Closing Browser
        rprint("[gold3][OK] Shutdown Browser[/gold3]")
        start_time = time.time()
        with Progress() as progress:
            task = progress.add_task("[cyan]Closing browser...", total=100)
            browser.close()
            progress.update(task, completed=100)
        rprint(
            f"[gold3][OK] Browser closed in {time.time() - start_time:.2f} seconds[/gold3]"
        )
