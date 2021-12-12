from common.by import By
from pom.page.demo_page import *
from pom.page.base_page import BasePage


class SearchDemo(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def execute_script_locator(self, locator):
        target = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", target)


