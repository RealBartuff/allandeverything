from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(by=By.NAME, value=self.locator))
        driver.find_element(by=By.NAME, value=self.locator).clear()
        driver.find_element(by=By.NAME, value=self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(by=By.NAME, value=self.locator))
        element = driver.find_element(by=By.NAME, value=self.locator)
        return element.get_attribute("value")
