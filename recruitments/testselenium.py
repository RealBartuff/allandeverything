# SALESmanago recruitment task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(PATH))
ebook_partial_name = "online_consumer"
data = {
    "name": "Bartłomiej Debowski",
    "email": "bartlomiej.debowski.benhauer+testrekrutacja@salesmanago.com",
    "company": "SALESmanago",
    "url": "www.salesmanago.pl",
    "phoneNumber": "123456789",
}


def fill_the_blanks(form_list, info):
    for k, v in info.items():
        for i in form_list:
            if i.get_attribute("name") == k:
                i.send_keys(v)
            elif i.get_attribute("id") == k:
                i.send_keys(v)
    return fill_the_blanks


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
    if ebook_partial_name in one:
        form = one
        break

driver.get(form)

edities = driver.find_elements(by=By.CLASS_NAME, value="form-control")
fill_the_blanks(edities, data)

submit_button = driver.find_element(by=By.CLASS_NAME, value="btn.center-block.form-btn")
submit_button.click()

time.sleep(3)

driver.quit()
