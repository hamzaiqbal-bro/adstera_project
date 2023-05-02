import requests
from urllib.parse import urlencode
import time
import random
from selenium.webdriver.support import expected_conditions as EC
# import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver as webDriver
from selenium.webdriver.support.wait import WebDriverWait

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


# def getFakeHeader():
#     response = requests.get(
#        url='https://headers.scrapeops.io/v1/browser-headers',
#        params={
#        'api_key': '5204fcb1-a9d5-47e9-a7f3-61af2b2b2f7e',
#        'num_headers': '1'}
#     )
#     # print('Response Body: ', response.json()['result'][0])
#     header = response.json()['result'][0]
#     print(header)

proxy_params = {
      'api_key': '5204fcb1-a9d5-47e9-a7f3-61af2b2b2f7e',
      'url': 'http://httpbin.org/ip',
  }

for lp in range(1000):
    # getFakeHeader()
    time.sleep(10)
    options = webDriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webDriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[0]})
    # driver.request_interceptor = header
    print(driver.execute_script("return navigator.userAgent;"))
    websiteUrl = random.choice(linkStrings)
    try:
        driver.get(websiteUrl)
    except:
        print("fuck")
    # websiteUrl = 'https://l.facebook.com/l.php?u=https%3A%2F%2Fgermanfashioninovation.blogspot.com%2F2023%2F04%2Fthe-future-of-german-fashion.html%3Ffbclid%3DIwAR3iqxn2tmqy9nt6Uap_X1iK6xVJZq_LcfjUHPmj-oneJ2hbG6IrUy_joAI&h=AT00GoDP3aLfpCVo0g1DNsW2a42P9k2fxIVas8IDImwbUlgO0KXQDjc9fm67asMoP0RlYw0Ox7CnUxmnb8ylUIEl39eMACfs-5FLssEpCCZRz2gNZSDqMUsrTYzxD-fG5B09F4bQ4p6VMfE'
    driver.implicitly_wait(15)
    time.sleep(10)
    print('choice url' + websiteUrl)
    if 'facebook' not in websiteUrl:
        driver.implicitly_wait(15)
        redictLink = driver.find_element(By.LINK_TEXT,"Link is here")
        redictLink.click()
        driver.implicitly_wait(15)
        last_height = driver.execute_script("return document.body.scrollHeight")
    else:
        driver.implicitly_wait(15)
        try:
            followLink = driver.find_element(By.LINK_TEXT, "Follow Link")
            followLink.click()
        except:
            print("No found")
        driver.implicitly_wait(15)
    # choiceNumber = random.choice(decisionArray)
    choiceNumber = 3

    if choiceNumber == 1:
        driver.maximize_window()
    elif choiceNumber == 2:
        last_height = driver.execute_script("return document.body.scrollHeight")
        print(last_height)
        try:
           driver.execute_script("window.scrollBy(0,"+randomNumberScrol+");")
        except:
            print('Not Found')
        time.sleep(random.randint(3,7))
    elif choiceNumber == 3:
        time.sleep(3)
        try:
            try:
                closeButton = driver.find_element(By.CLASS_NAME, "pl-c249f3b6c7e1090751716aba1376c563__closelink")
                closeButton.click()
            except:
                print('Not Found')
            driver.implicitly_wait(10)
            searchButton = driver.find_element(By.ID, "nav-search")
            searchButton.click()
        except:
            print("An exception occurred in search section")
    elif choiceNumber == 4:
        try:
            backButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div/ul/li[1]")
            backButton.click()
        except:
            print("An exception occurred in backbutton")
    elif choiceNumber == 5:
        driver.maximize_window()
        time.sleep(random.randint(5, 10))
        try:
            redditlogo = driver.find_element(By.CLASS_NAME, "reddit")
            redditlogo.click()
        except:
            print("An exception occurred in reddit logo")
    elif choiceNumber == 6:
        try:
            popularPost1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/div[3]/div[1]/div[2]/div[3]")))
            popularPost1.click()
        except:
            print("An exception occurred in popular post")
    elif choiceNumber == 7:
        try:
            popularPost3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]")
            popularPost3.click()
        except:
            print("An exception occurred in popular 3")
    # elif choiceNumber == 8:
    #     driver.execute_script("window.scrollBy(0,600);")
    #     beautyPost1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/a")
    #     beautyPost1.click()
    elif choiceNumber == 9:
        driver.execute_script("window.scrollBy(0,600);")
        try:
            tag1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/div[3]/div[3]/div[2]/ul/li[1]")))
            tag1.click()
        except:
            print("An exception occurred in tags")
    elif choiceNumber == 10:
        driver.execute_script("window.scrollBy(0,600);")
        try:
            tag2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/div[3]/div[3]/div[2]/ul/li[2]")))
            tag2.click()
        except:
            print("An exception occurredin tag 2")
    elif choiceNumber == 11:
        driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(random.randint(0,9))
        try:
            bottomToUp = driver.find_element(By.XPATH, "/html/body/div[4]")
            time.sleep(random.randint(3, 9))
            bottomToUp.click()
        except:
            print("An exception occurred in bottom up")

    time.sleep(random.randint(0, 5) * 60)
    driver.quit()
    time.sleep(random.randint(0, 2) * 60)
