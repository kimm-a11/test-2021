import logging
from selenium.webdriver.remote.webelement import WebElement
from common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

Timeout = 10

ElementStat = {
    'By.Visibility': ec.visibility_of_element_located,
    'By.Presence': ec.presence_of_element_located

}


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("点击操作")
    def is_click(self, locator):
        self.find_element(locator).click()

    def find_element(self, locator, tag="By.Presence") -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout=Timeout).until(ElementStat[tag](locator))
        except AssertionError:
            return AssertionError

    def get_current_url(self):
        return self._driver.current_url

    def open_url(self, url):
        return self._driver.get(url)

    def is_element_text(self, locator):
        return self.find_element(locator).text

    @property
    def execute_script(self):
        """

        arguments[0].scrollIntoView()
        window.scrollTo(0,document.body.scrollHeight)
        """
        return self._driver.execute_script