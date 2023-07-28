import subprocess
import time
from bs4 import BeautifulSoup

def run_scrape():
    while True:
        print("Starting new Scrape instance...")
        p = subprocess.Popen(["C:\\Users\\ojadi\\PycharmProjects\\marketPlace\\venv\\Scripts\\python.exe", "main.py"])
        print("Now waiting to start again")
        time.sleep(600)
        print("terminate")# Wait for 30 minutes
        p.terminate()  # Terminate the process

run_scrape()

import sys
print(sys.executable)
 