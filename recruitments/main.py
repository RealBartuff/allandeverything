import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page

# PATH = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'chromedriver')
PATH = "C:\Program Files (x86)\chromedriver.exe"
website = "http://www.salesmanago.com"


class SalesmanagoComSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(PATH))
        self.driver.get(website)

    def test_search_in_salesmanago_com(self):

        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "https://www.salesmanago.com/info/knowledgecenter.htm"
        main_page.click_go_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
