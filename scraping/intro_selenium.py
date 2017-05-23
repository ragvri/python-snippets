import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://ww1.gogoanime.io/pokemon-sun-moon-episode-21')  # goes to specific page

# waiting for the page to load for max time =10
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "btndownload")))
except Exception as e:
    print(e)

download = browser.find_element_by_class_name('btndownload')
download.click()
time.sleep(5)
link_download = browser.find_element_by_class_name("dowload")
print(link_download)
browser.quit()
