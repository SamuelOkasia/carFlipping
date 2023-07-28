import subprocess
import time
import threading
import requests

from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

from urllib.parse import urlparse, parse_qs

import re

import carChrome

def priceExctract(span):
    price = re.search(r'£(\d+,\d+)', span)
    if price:
        price = int(price.group(1).replace(',', ''))
    if type(price) == int:
        return price
    else:
        return span


class Scrape:
    def __init__(self):
        try:
            subprocess.run(['taskkill', '/F', '/IM', 'firefox.exe'])
        except:
            pass

        firefox_profile_path = r'C:\\Users\\ojadi\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p4n04sri.default-release'  # Replace with the path of your Firefox profile
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        options.add_argument("-profile")
        options.add_argument(firefox_profile_path)
        service = Service('geckodriver.exe')
        self.driver = Firefox(service=service, options=options)
        self.driver.get("https://www.facebook.com/marketplace/london/search?query=vw%20polo")
        self.acceptCookies()
        actions = ActionChains(self.driver)
        time.sleep(3)
        actions.move_by_offset(10, 10).perform()
        threading.Thread(target=self.getSoup()).start()


    def acceptCookies(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")))
            element.click()
        except Exception as e :
            pass
            #print("No cookie accept button detected")

    def getSoup(self):
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            giveSoup = takeInSoup(soup)



class takeInSoup:
    def __init__(self,soup):
        self.years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
                      '2022']
        self.cars = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            for i,div in enumerate(soup.findAll(class_= "xjp7ctv")):
                self.name = div.find(class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
                self.price = self.getPrice(div)
                self.mileage = self.getMileage(div)
                self.href = self.getHref(div)

                self.isPriceLower = int(self.price) < 4000
                self.found_years = any([year in str(self.name) for year in self.years])
                self.isMileageLower = self.mileage < 100
                self.alreadySeenIt = self.check_string_in_file(self.href)
                #print(self.price, self.mileage, self.alreadySeenIt)

                if (self.isPriceLower and self.found_years and self.isMileageLower) and (not self.alreadySeenIt):
                    #self.filtered_cars(div, name, price, mileage,href)
                    #executor.submit(self.filtered_cars, div, name, price, mileage, href)
                    executor.submit(carChrome.car_page,self.href,self.mileage,self.price)
                    #print("Found Div")

                    with open('car_href.txt', 'a') as f:
                        f.write(str(self.href + '\n'))
    def check_string_in_file(self,href):
        with open("car_href.txt", 'r') as self.read_obj:
            for line in self.read_obj:
                if urlparse(href).path in line:
                    return True
            return False

    def filtered_cars(self, div, name, price,mileage,href):
        carChrome.car_page(href, mileage, price)

    def getHref(self,div):
        try:
            a_tag = div.find('a')
            href = a_tag.get('href')
            #print("Href Found")
            return "https://www.facebook.com/" + str(href)
        except:
            #print(div)
            return "https://www.facebook.com/marketplace/item/298021172628300/?ref=search&referral_code=null&referral_story_type=post&tracking=browse_serp%3A7d9a4ad7-21d9-4e4b-a1dc-29f2274586c4"
    def getPrice(self,div):
        price = div.find(
            class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u")
        price = (priceExctract(str(price)))

        if type(price) != int:
            return 100000
        else:
            return price

    def getMileage(self,div):
        mileage = ''
        mileage_list = div.find_all(class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84")
        for m in mileage_list:
            if "km" in str(m):
                mileage = m
        pattern = r'(\d+)K km'
        match = re.search(pattern, str(mileage))
        if match:
            return int(match.group(1))
        else:
            return 200






scrape_instance = Scrape()

