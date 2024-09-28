# This is for making a fake progress bar

import time
from rich.progress import track


def progbar():
    for i in track(range(20), description="Processing..."):
        time.sleep(1)  # Simulate work being done
