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

ifttt_key = 'key_from_ifttt'
print('key for notification', ifttt_key)

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/<user>/.config/google-chrome")

driver = webdriver.Chrome(options=options,executable_path='./chromedriver') 
# driver = webdriver.Chrome(executable_path='./chromedriver') 

xbox_x_url = 'https://www.amazon.fr/RRT-00010-Microsoft-Xbox-Series-X/dp/B08K3F3VQG/'
xbox_s_url = 'https://www.amazon.fr/Xbox-Console-Next-Gen-compacte-digitale/dp/B087VM5XC6/'
ps5_url = 'https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/'
switch_url = 'https://www.amazon.fr/Nintendo-Switch-avec-paire-Rouge/dp/B07WKNQ8JT'

driver.get(ps5_url)

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'add-to-cart-button')))
print("found the element!")
driver.find_element_by_id('add-to-cart-button').click()
res = requests.post('https://maker.ifttt.com/trigger/detect_ps/json/with/key/{}'.format(ifttt_key), 
headers={"Content-Type": "application/json"},
json={'detected at':datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
)

driver.quit()
