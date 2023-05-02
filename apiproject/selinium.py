import time
from selenium import webdriver


useragentarray = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
]

chromedriver_autoinstaller.install(cwd=True)
options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[0]})
print(driver.execute_script("return navigator.userAgent;"))
driver.get('https://www.samsclub.com/')


# hit return after you enter search text
time.sleep(5) # slee
last_height = driver.execute_script("return document.body.scrollHeight")
print(last_height)
driver.execute_script("window.scrollTo(0, 3000);")
# p for 5 seconds so you can see the results
time.sleep(100)
driver.quit()
