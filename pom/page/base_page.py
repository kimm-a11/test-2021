from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
from common.loger import logger
from common.base_config import Timeout
import traceback
import sys
from selenium.webdriver.support.color import Color
ElementStat = {
    'By.Visibility': ec.visibility_of_element_located,
    'By.Presence': ec.presence_of_element_located,
    'By.Clickable': ec.element_to_be_clickable,
    'By.Multi_Visibility': ec.visibility_of_all_elements_located,
    'By.Multi_Presence': ec.presence_of_all_elements_located,

}


class BasePage:
    input = (By.CSS_SELECTOR, '[id="kw"]')  # 输入框
    submit_btn = (By.CSS_SELECTOR, '[type="submit"]')  # 提交按钮
    all_page = (By.CSS_SELECTOR, '[class="cur-tab"]')  # all页面

    def __init__(self, driver):
        self._driver = driver

    @allure.step("点击操作")
    def is_click(self, locator):
        self.find_element(locator).click()

    def find_element(self, locator, tag="By.Presence") -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout=Timeout).until(ElementStat[tag](locator))

        except TimeoutException as e:
            logger.info('报错啦{}', sys.exc_info())
            raise e

    def find_elements(self, locator, tag="By.Multi_Presence"):
        try:
            return WebDriverWait(self._driver, timeout=Timeout).until(ElementStat[tag](locator))
        except TimeoutException as e:
            logger.info('报错啦{}',sys.exc_info())
            raise e

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

    def input_text(self, locator, text):
        self.is_click(locator)
        self.find_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return [item.tetx for item in self.find_elements(locator)]

    def get_attribute_value(self, locator, name):
        return self.find_element(locator).get_attribute(name)

    def get_attribute_values(self, locator, name):
        return [item.get_attribute(name) for item in self.find_elements(locator)]

    def judge_jump_url(self, url, default=True, timeout=Timeout):
        try:
            if default:
                WebDriverWait(self._driver, timeout).until(ec.url_changes(url))
            else:
                WebDriverWait(self._driver, timeout).until(ec.url_contains(url))
        except:
            self.execute_script("window.stop()")
        finally:
            if default:
                return self.get_current_url() != url
            return url in self.get_current_url()

    def get_css_property(self):
        return self.find_element(locator).value_of_css_property(name)

    def get_css_propertys(self, locator, name):
        return [item.value_of_css_property(name) for item in self.find_elements(locator)]

    def string_to_hex(self,data):
        return Color.from_string(data).hex