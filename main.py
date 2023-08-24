# main.py

from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

service = Service()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognite")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=chrome_options)



@app.route("/")
def main():
    driver.get(url="https://github.com/docker")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/main/div/header/div[1]/div/div[2]/div[1]/div")))
    desc_str = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/header/div[1]/div/div[2]/div[1]/div")
    return desc_str.text