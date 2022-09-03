# SALESmanago recruitment task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(PATH))

driver.get("https://www.salesmanago.com/")
sources = driver.find_elements(by=By.CLASS_NAME, value="menu__link.menu__item--show")
for elem in sources:
    if elem.get_attribute("data-number") == "3":
        resources = elem
        break

ebooks = resources.find_element(by=By.CLASS_NAME, value="category__item").get_attribute("href")
driver.get(ebooks)

get_ebook = driver.find_elements(by=By.CLASS_NAME, value="col-lg-3.ebook__text")
for ebook in get_ebook:
    one = ebook.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    if "online_consumer" in one:
        form = one
        break

driver.get(form)

edities = driver.find_elements(by=By.CLASS_NAME, value="form-control")
for i in edities:
    if i.get_attribute("name") == "name":
        i.send_keys("Bartłomiej Debowski")
    elif i.get_attribute("id") == "email":
        i.send_keys("bartlomiej.debowski@salesmanago.com")
    elif i.get_attribute("name") == "company":
        i.send_keys("SALESmanago")
    elif i.get_attribute("name") == "url":
        i.send_keys("www.salesmanago.pl")
    elif i.get_attribute("name") == "phoneNumber":
        i.send_keys("123456789")

submit_button = driver.find_element(by=By.CLASS_NAME, value="btn.center-block.form-btn")
submit_button.click()

time.sleep(3)

driver.quit()
