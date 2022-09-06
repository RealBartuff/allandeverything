import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page

PATH = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'chromedriver')
website = "http://www.salesmanago.com"


class SalesmanagoComSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(PATH))
        self.driver.get(website)

    def test_download_ebook(self):
        main_page = page.MainPage()
        main_page.search_text_element = "data-number"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
