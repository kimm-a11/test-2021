import locale
import logging
from pom.page.base_page import BasePage
from common.by import By
from common.base_config import html
Timeout = 10


class TestDemo(BasePage):
    username = (By.XPATH, '//input[@id="username"]')  # 用户名
    loginPWD = (By.XPATH, '//input[@id="loginPWD"]')  # 密码
    login = (By.XPATH, '//button[@id="surelogin"]')  # 登录

    def __init__(self, driver):
        super().__init__(driver)

    def login_s(self):
        self.open_url(html)
        self.is_click(self.username)
        self.find_element(self.username).send_keys('17521016982')
        self.is_click(self.loginPWD)
        self.find_element(self.loginPWD).send_keys('123456')
        self.is_click()


