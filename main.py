from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import requests
import json
from datetime import datetime

import time
import os
import logging

ifttt_key = None
print('key for notification', ifttt_key)

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/mo/.config/google-chrome")

driver = webdriver.Chrome(options=options,executable_path='./chromedriver') 
time.sleep(5)
# driver = webdriver.Chrome(executable_path='./chromedriver') 

xbox_x_url = 'https://www.amazon.fr/RRT-00010-Microsoft-Xbox-Series-X/dp/B08K3F3VQG/'
xbox_s_url = 'https://www.amazon.fr/Xbox-Console-Next-Gen-compacte-digitale/dp/B087VM5XC6/'
ps5_url = 'https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/'
switch_url = 'https://www.amazon.fr/Nintendo-Switch-avec-paire-Rouge/dp/B07WKNQ8JT'
tp_link = 'https://www.amazon.fr/dp/B073D621PC?smid=A1X6FK5RDHNB96&th=1&psc=1'

def check(url,action='reserve'):
    element_ids = {
        'buy':'buy-now-button',
        'reserve': 'add-to-cart-button'
    }
    element_id = element_ids[action]
    try:
        driver.get(url)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, element_id)))
        print("found the element!")
        driver.find_element_by_id(element_id).click()
        res = requests.post('https://maker.ifttt.com/trigger/detect_ps/json/with/key/{}'.format(ifttt_key), 
        headers={"Content-Type": "application/json"},
        json={'detected at':datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
        )
        logging.info(res.status_code)
        return True
    except:
        logging.warning("nothing found")
        return False


FOUND_FLAG = False

try:
    while not FOUND_FLAG:
        time.sleep(60)
        logging.info("checking url...")
        FOUND_FLAG = check(ps5_url,action='buy')
except KeyboardInterrupt:
    print('stopping the driver...')
    driver.quit()

driver.quit()