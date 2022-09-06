from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.TAG_NAME, 'data-number')


class EbooksPageLocators(object):

    GO_BUTTON = (By.CLASS_NAME, 'col-lg-3.ebook__text')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
