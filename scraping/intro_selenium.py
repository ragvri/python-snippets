from selenium import webdriver                    #webdriver actually allows us to open the browser
from selenium.webdriver.common.by import By       #By allows to search for specific parameters
from selenium.webdriver.support.ui import WebDriverWait  #WebdriveWait allows for the page to load
from selenium.webdriver.support import expected_conditions as EC   #allows us to specify conditions deciding that the webpage has loaded
from selenium.common.exceptions import TimeoutException


#allows us to open the page in incognito mode
option=webdriver.ChromeOptions()
option.add_argument("--incognito")

#create a new instance of chrome in incognito mode
#we need to specify the path where the chrome driver is located (use command : which chromedriver)
browser=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",chrome_options=option)

#go to the specific page
browser.get("https://finance.yahoo.com/quote/FB/?p=FB")

#wait upto 10s for the page to load
timeout=20
try:
    WebDriverWait(browser,timeout=timeout).until(EC._element_if_visible(By.XPATH,""))
