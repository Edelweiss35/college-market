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
        self.college_name = "University of Florida"
        self.link = "https://orgs.studentinvolvement.ufl.edu/Organizations"
        
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
        chrome_options.add_argument("--headless")
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
        org_list = []

        showing_num_part = drive.find_element_by_xpath("//div[@class='form-control-static']/a").click()
        iwait = random.randint(1, 2) + random.random()
        time.sleep(iwait)
        showing_select = drive.find_element_by_xpath("//div[@class='form-control-static']/form/div/select").click()
        iwait = random.randint(1, 2) + random.random()
        time.sleep(iwait)
        drive.find_element_by_xpath("//div[@class='form-control-static']/form/div/select/option[@label='96']").click()
        iwait = random.randint(1, 2) + random.random()
        time.sleep(iwait)

        idx = 1
        while True:
            try:
                drive.find_element_by_xpath("//ul/li/a[text()='{}']".format(idx)).click()
                iwait = random.randint(2, 3) + random.random()
                time.sleep(iwait)

                org_obj_list = drive.find_elements_by_xpath("//div/h2[@class='box-title']/a")
                for org_obj in org_obj_list:
                    org = {}
                    org['college_name'] = self.college_name
                    org['org_name'] = org_obj.text
                    org['link'] = org_obj.get_attribute('href')
                    org['email'] = 'n/a'
                    org_list.append(org)
                idx = idx + 1
            except Exception as e:
                break
        
        df = pd.DataFrame(org_list)
        # print(df)
        fpath = 'result/' + self.college_name + ' - Market Research.xlsx'
        # print(fpath)
        df.to_excel(fpath)
        print(len(org_list))

with Bot() as scraper:
    scraper.browser_init()
    scraper.main()