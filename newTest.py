from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile_directory = r'Profile 1'  # replace 'Profile 1' with your profile's name
user_data_dir = r"C:\Users\ojadi\AppData\Local\Google\Chrome\User Data"

print("Opening chrome")
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_directory}")
#chrome_options.add_argument("--headless")  # Ensure GUI is off
print("Chrome opened")

#if not working try: pip install webdriver_manager --upgrade
webdriver_service = Service(ChromeDriverManager().install())
ddriver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
ddriver.get("www.google.co.uk")
