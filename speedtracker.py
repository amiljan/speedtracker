from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%Y %H:%M")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://fast.com/")

wait = WebDriverWait(driver,60)
status = wait.until(EC.visibility_of_element_located((By.ID, "show-more-details-link")))

if status != None:
    speed = driver.find_element(By.ID,"speed-value").text
    unit = driver.find_element(By.ID,"speed-units").text
    speed_table = open("/home/amiljan@reversinglabs.lan/bin/speedtracker/speed_table.csv","a")
    speed_table.write(f'{date};{speed}{unit}\n')

driver.close()