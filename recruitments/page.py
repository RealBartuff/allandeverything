from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.by import By


class SearchSourceElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'href'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_source_element = SearchSourceElement()

    def locate_ebooks(self):
        """Triggers the search"""
        location = self.driver.find_element(*MainPageLocators.EBOOKS_BUTTON)
        location.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
