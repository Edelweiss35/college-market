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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import pickle


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID_input = '1ebSulg2GIE43gQ4es6BTCgSYplccncy74mRG4VPUoGU'
SAMPLE_RANGE_NAME = 'In Queue!A2:AA50'

global values_input, service
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)  # here enter the name of your downloaded JSON file
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)


class Bot:
    def __init__(self):
        self.college_name = ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        try:
            if self.drive is not None:
                self.drive.quit()
        except Exception as e:
            pass

    def readGoogleSheet(self, idx):
        self.idx = idx
        # Call the Sheets API
        sheet = service.spreadsheets()
        result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                          range=SAMPLE_RANGE_NAME).execute()
        values_input = result_input.get('values', [])
        # print(values_input)
        if not values_input:
            print('No data found.')
            return False
        else:
            try:
                self.link = values_input[idx][1]
                self.college_name = values_input[idx][0]
                return True
            except Exception as e:
                print('{} row is empty or wrong. Please check it again.'.format(str(idx + 1)))
                return False

    def updateGoogleSheet(self):
        value_input_option = "USER_ENTERED"
        value_range_body = {
            "values": [
                [
                    "Done!",
                    "Moved to Completed"
                ]
            ],
            "majorDimension": "DIMENSION_UNSPECIFIED"
        }
        sheet = service.spreadsheets()
        result_input = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID_input, range='In Queue!A{}:C5'.format(self.idx + 2),
                                             valueInputOption=value_input_option, body=value_range_body)
        result_input.execute()

        value_range_body = {
            "values": [
                [
                    self.college_name,
                    self.link,
                    "Campus Lab"
                ]
            ],
            "majorDimension": "DIMENSION_UNSPECIFIED"
        }
        sheet = service.spreadsheets()
        result_input = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                             range='Completed!A:C',
                                             valueInputOption=value_input_option, body=value_range_body)
        result_input.execute()

    def browser_init(self):
        try:
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
        except Exception as e:
            print('googlesheet error')
            pass

    def main(self):
        try:
            drive = self.drive
            while True:
                try:
                    drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    more_button = drive.find_element_by_xpath("//div[@class='outlinedButton']/button/div/div/span")
                    drive.execute_script("arguments[0].click();", more_button)
                    iwait = random.randint(2, 3) + random.random()
                    time.sleep(iwait)
                except Exception as e:
                    break
            org_obj_list = drive.find_elements_by_xpath("//div[@id='org-search-results']/div/div/div/a")
            print(len(org_obj_list))
            org_href_list = []
            org_list = []
            for org_obj in org_obj_list:
                href = org_obj.get_attribute('href')
                org_href_list.append(href)
            for org_href in org_href_list:
                drive.get(org_href)
                print(org_href)
                iwait = random.randint(3, 5) + random.random()
                time.sleep(iwait)
                org = {}
                org['college_name'] = self.college_name
                try:
                    org['org_name'] = drive.find_element_by_xpath("//div/div/div/h1").text
                except Exception as e:
                    continue
                org['link'] = org_href
                try:
                    org['email'] = drive.find_element_by_xpath("//div/div/strong[contains(text(), 'E:')]/parent::div").text.replace('Contact Email\nE: ', '')
                except Exception as e:
                    org['email'] = 'n/a'
                org_list.append(org)
            df = pd.DataFrame(org_list)
            fpath = 'result/' + self.college_name + ' - Market Research.xlsx'
            df.to_excel(fpath)
            print(len(org_list))
        except Exception as e:
            print('googlesheet error')
            pass
