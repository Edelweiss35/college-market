import os
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import random
import logging
import pandas as pd


class Bot:
    def __init__(self):
        self.college_name = "Florida State University"
        self.link = "https://fsu.campuslabs.com/engage/organizations"
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        try:
            if self.drive is not None:
                self.drive.quit()
        except Exception as e:
            pass

    def browser_init(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-errors')
        drive = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        drive.get(self.link)
        iwait = random.randint(2, 3) + random.random()
        time.sleep(iwait)
        self.drive = drive
    
    def main(self):
        drive = self.drive

        while True:
            try:
                drive.find_element_by_xpath("//div[@class='outlinedButton']/button").click()
                iwait = random.randint(1, 2) + random.random()
                time.sleep(iwait)
            except Exception as e:
                break

        org_obj_list = drive.find_elements_by_xpath("//div[@id='org-search-results']/div/div/div/a")
        print(len(org_obj_list))
        org_href_list = []
        for org_obj in org_obj_list:
            href = org_obj.get_attribute('href')
            org_href_list.append(href)

        org_list = []
        for org_href in org_href_list:
            drive.get(org_href)
            iwait = random.randint(2, 3) + random.random()
            time.sleep(iwait)
            org = {}
            org['college_name'] = self.college_name
            org['org_name'] = drive.find_element_by_xpath("//div/div/div/h1").text
            org['link'] = org_href
            try:
                org['email'] = drive.find_element_by_xpath("//div/div/strong[contains(text(), 'E:')]/parent::div").text.replace('Contact Email\nE: ', '')
            except Exception as e:
                org['email'] = 'n/a'
            org_list.append(org)
            # print(org)
        # print(org_list)

        df = pd.DataFrame(org_list)
        # print(df)
        fpath = 'result/' + self.college_name + ' - Market Research.xlsx'
        # print(fpath)
        df.to_excel(fpath)
        print(len(org_list))

with Bot() as scraper:
    scraper.browser_init()
    scraper.main()