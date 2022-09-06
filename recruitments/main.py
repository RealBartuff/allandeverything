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
        x = main_page.search_source_element
        x.locate_ebooks()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
