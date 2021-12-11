from common.by import By
from pom.page.demo_page import *
from pom.page.base_page import BasePage


class SearchDemo(BasePage):
    next_page = (By.XPATH, "//a[text()='下一章']")  # 下一章按钮
    login = (By.CSS_SELECTOR, '[class="login_tips"] [rel="nofollow"]')  # 下一章按钮
    blog = (By.CSS_SELECTOR, '[id="blog_nav_sitehome"]')  # 下一章按钮

    def __init__(self, driver):
        super().__init__(driver)

    def execute_script_locator(self, locator):
        target = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", target)


