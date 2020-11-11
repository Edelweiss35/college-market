import os
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import random
import logging


class Bot:
    def __init__(self):
        logging.warning('start running...')
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        try:
            if self.drive is not None:
                self.drive.quit()
        except Exception as e:
            pass

    def browser_init(self, metadata):
        self.metadata = metadata
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-errors')
        drive = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        drive.get(self.metadata['link'])
        iwait = random.randint(2, 3) + random.random()
        time.sleep(iwait)
        self.drive = drive
    
    def main(self):
        logging.warning('')

