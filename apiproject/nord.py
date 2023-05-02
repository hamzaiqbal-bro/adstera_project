import platform
import random
import os
import time

from selenium.webdriver.common.by import By

windows_countries = ['United States', 'Canada', 'Argentina', 'Brazil', 'Mexico', 'Costa Rica', 'Chile',
                     'United Kingdom', 'Germany', 'France', 'Netherlands', 'Sweden', 'Switzerland',
                     'Denmark', 'Poland', 'Italy', 'Spain', 'Norway', 'Belgium', 'Ireland', 'Czech Republic',
                     'Austria', 'Portugal', 'Finland', 'Ukraine', 'Romania', 'Serbia', 'Hungary', 'Luxembourg',
                     'Slovakia', 'Bulgaria', 'Latvia', 'Greece', 'Iceland', 'Estonia', 'Albania', 'Croatia',
                     'Cyprus', 'Slovenia', 'Moldova', 'Bosnia and Herzegovina', 'Georgia', 'North Macedonia',
                     'Turkey', 'South Africa', 'India', 'Israel', 'Turkey', 'United Arab Emirates', 'Australia',
                     'Taiwan', 'Singapore', 'Japan', 'Hong Kong', 'New Zealand', 'Malaysia', 'Vietnam', 'Indonesia',
                     'South Korea', 'Thailand']

def nordvpn():
    server = "nordvpn -c -g \'"+random.choice(windows_countries)+"\'"+" > /dev/null 2>&1"
    os.system(server)
    time.sleep(10)


import requests
ip = requests.get('https://api.ipify.org').text
print(f"\nBefore Using NordVpn\nIp:\t{ip}")


nordvpn()

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://api.ipify.org')
ip = driver.find_element(By.TAG_NAME,"body").text
print(f"\nWith Selenium\nIp:\t{ip}")
driver.close()
