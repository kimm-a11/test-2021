import logging
from pom.page.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

Timeout = 10

ElementStat = {
    By.Visibility: ec.visibility_of_element_located

}


class TestDemo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


