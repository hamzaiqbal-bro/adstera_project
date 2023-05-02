import requests
from urllib.parse import urlencode
import time
import random
from selenium.webdriver import DesiredCapabilities
from seleniumwire import webdriver as webDriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
# import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import seleniumwire.undetected_chromedriver as uc


proxy = ''
header = {}
randomNumberScrol = str(random.randint(-15, 3000))
decisionArray = [1,2,3,4,5,6,7,9,10,11]
last_height = 0
linkStrings = [
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12s9sjg/blog/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12s9rr9/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12s9prj/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12ujp7n/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12ujopg/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12ujo4h/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://www.reddit.com/user/Big-Mulberry-5231/comments/12ujng4/blog_post/?utm_source=share&utm_medium=web2x&context=3',
    'https://l.facebook.com/l.php?u=https%3A%2F%2Fgermanfashioninovation.blogspot.com%2F2023%2F04%2Fthe-ultimate-guide-to-beauty-in-germany.html%3Ffbclid%3DIwAR0zgmWDhRbuIw692yC0qz9Nj57qT91yJfKOy-jcJhd9rk1-csCtLj90Lyo&h=AT1_ilu3GdULKIAfR1DE-Q8T0xNKWIM7GDNqmjmofsqWViCaNvaSWem8kizQ1e85U_UztwC1Inh9WFznxWTJvNxX-ncIvfQYqzkoGvplE_5Yl25Jqu9xhGW2jwbmMmqQ7DD5XROKqobVxfE',
    'https://l.facebook.com/l.php?u=https%3A%2F%2Fgermanfashioninovation.blogspot.com%2F2023%2F04%2Fbeauty-on-budget.html%3Ffbclid%3DIwAR3o5SLrz20c81pZJkLETbqi0b2xGT2KlFcJMcZ04LenGcWS7B-6lASvMVs&h=AT34t9izO33OIPMUHqIVZQgTnhBwi_ayAm3_aw43UXHmMgs19LYgxPqg0AcbzQjP0UCiD-QSFwgO-RefRVk-OxuY4F1qRCuQN7FrAkrqKY-MQzaMy2jhzOKoMwjCoBJjqYZmo2mmJUvkSV0',
    'https://l.facebook.com/l.php?u=https%3A%2F%2Fgermanfashioninovation.blogspot.com%2F2023%2F04%2Fthe-future-of-german-fashion.html%3Ffbclid%3DIwAR3iqxn2tmqy9nt6Uap_X1iK6xVJZq_LcfjUHPmj-oneJ2hbG6IrUy_joAI&h=AT00GoDP3aLfpCVo0g1DNsW2a42P9k2fxIVas8IDImwbUlgO0KXQDjc9fm67asMoP0RlYw0Ox7CnUxmnb8ylUIEl39eMACfs-5FLssEpCCZRz2gNZSDqMUsrTYzxD-fG5B09F4bQ4p6VMfE'
]


def getFakeHeader():
    response = requests.get(
       url='https://headers.scrapeops.io/v1/browser-headers',
       params={
       'api_key': '557ddf38-f057-4f1a-8eb6-90017ab257a4',
       'num_headers': '1'}
    )
    # print('Response Body: ', response.json()['result'][0])
    header = response.json()['result'][0]
    print(header)

proxy_params = {
      'api_key': '557ddf38-f057-4f1a-8eb6-90017ab257a4',
      'url': 'http://httpbin.org/ip',
  }

SCRAPEOPS_API_KEY = '557ddf38-f057-4f1a-8eb6-90017ab257a4'

proxy_options = {
    'proxy': {
        'http': f'http://scrapeops.headless_browser_mode=true:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353',
        'https': f'http://scrapeops.headless_browser_mode=true:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353',
        'no_proxy': 'localhost:127.0.0.1'
    }
}

def getIp():
    response = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': '557ddf38-f057-4f1a-8eb6-90017ab257a4',
            'url': 'https://quotes.toscrape.com/',
        },
    )
    print('Body: ', response.content)
    # print(response.json()['origin'])
    # proxy = str(response.json()['origin'])

for lp in range(1000):
    getIp()
    getFakeHeader()
    time.sleep(10)
    options = webDriver.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    options.add_argument("--disable-bundled-ppapi-flash")  # Disable internal Flash player
    options.add_argument("--disable-plugins-discovery")
    driver = webDriver.Chrome(ChromeDriverManager().install(),options=options,seleniumwire_options=proxy_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[0]})
    driver.request_interceptor = header
    print(driver.execute_script("return navigator.userAgent;"))
    websiteUrl = random.choice(linkStrings)
    driver.get('https://www.expressvpn.com/what-is-my-ip')
