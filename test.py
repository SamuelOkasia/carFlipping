from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


profile_directory = r'Profile 1'  # replace 'Profile 1' with your profile's name
user_data_dir = r"C:\Users\ojadi\AppData\Local\Google\Chrome\User Data"

"""
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_directory}")
#chrome_options.add_argument("--headless")  # Ensure GUI is off

webdriver_service = Service(ChromeDriverManager().install())
ddriver = webdriver.Chrome(service=webdriver_service ,options=chrome_options)
ddriver.get("https://www.facebook.com/marketplace/item/285247360675462/?ref=browse_tab&referral_code=marketplace_top_picks&referral_story_type=top_picks")
"""
inputt = input("Paste: ")
with open("car_href.txt", 'r') as read_obj:
    for line in read_obj:
        if str(inputt) in line:
            print("Already seen it")

from urllib.parse import urlparse, parse_qs

url = "https://www.facebook.com//marketplace/item/817475652975151/?ref=search&referral_code=null&referral_story_type=post&tracking=browse_serp%3A3bca2960-d4ff-4156-9a96-215405626c20&__tn__=!%3AD"


parsed_url = urlparse(inputt)
path = parsed_url.path
print(f'Path: {path}')