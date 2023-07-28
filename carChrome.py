import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

from urllib.parse import urlparse, parse_qs

# s

class car_page:
    def __init__(self,url,mileage,price):
        print("Chrome Opens")
        self.url = url
        self.PushUrl = "https://api.pushover.net/1/messages.json"
        self.mileage = mileage
        self.price = price

        profile_directory = r'Profile 1'  # replace 'Profile 1' with your profile's name
        user_data_dir = r"C:\Users\ojadi\AppData\Local\Google\Chrome\User Data"

        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={user_data_dir}")
        chrome_options.add_argument(f"profile-directory={profile_directory}")
        chrome_options.add_argument("--headless")  # Ensure GUI is off

        webdriver_service = Service(ChromeDriverManager().install())
        ddriver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
        ddriver.get(self.url)

        try:
            element = WebDriverWait(ddriver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME,"x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67")))
            element.click()
        except Exception as e:
            pass
            #print("No cookie accept button detected Chrome")


        self.html = ddriver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')

        self.transmission = self.getTransmission()

        self.colour = self.getColour()

        time.sleep(2)
        self.name = "Default{Polo}"
        self.name_list = self.soup.find_all(class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u")
        print(len(self.name_list))
        for n in self.name_list:
            if "Chats" not in n.text:
                self.name = n.text

        self.isNotWhite = "White" not in str(self.name)

        #print(self.url," Is not white: ",Sself.isNotWhite)



        if self.transmission.replace(" ","") != "Automatic" and 1==1: #and self.colour.replace(" ","") == "Black"
            self.message = str(self.name) + " " + self.colour + " " + str(self.mileage) + "000 km  £" + str(
                self.price) + " " + str(self.url)
            print(self.message)
            data = {
                "token": "a5ue756cfjcdqip995j94kiw9v46nz",
                "user": "u5mf5gqgyd8i8w528p9oy2uxc1m85p",
                "message":  self.message
            }

            dataMichael = {
                "token": "a5ue756cfjcdqip995j94kiw9v46nz",
                "user": "u4egksi8cbyx8y6s26fcuv56o599g7",
                "message": self.message
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }

            response = requests.post(self.PushUrl, data=data, headers=headers)
            responseMichael = requests.post(self.PushUrl, data=dataMichael, headers=headers)

            print(response.text)

        else:
            print(str(self.name) + " " + str(self.mileage) + "000 km  £" + str(self.price) + "\n")

        ddriver.quit()

    def getTransmission(self):
        tr = self.soup.find_all(
            class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u")
        for t in tr:
            if "transmission" in str(t):
                return t.text.replace(" transmission",'')
        print("No transmission Stated")
        return "No Transmission Stated"

    def getMileage(self):
        tr = self.soup.find_all(
            class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u")
        for t in tr:
            if "transmission" in str(t):
                return t.text.replace(" transmission", '')
        print("No transmission Stated")
        return "No Transmission Stated"

    def getColour(self):
        tr = self.soup.find_all(
            class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u")
        for t in tr:
            if "Exterior colour:" in t.text:
                exterior_Colour = t.text.split("·")
                return exterior_Colour[0].replace("Exterior colour: ",'')

        return "No Colour Stated"