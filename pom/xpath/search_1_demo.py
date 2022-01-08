from common.by import By
from pom.page.demo_page import TestDemo
from pom.page.base_page import BasePage
from common.base_config import html
class SearchDemo(BasePage):
    username = (By.XPATH, '//input[@id="username"]')  # 用户名
    loginPWD = (By.XPATH, '//input[@id="loginPWD"]')  # 密码
    login = (By.XPATH, '//button[@id="surelogin"]')  # 登录


    upload_0 = (By.XPATH, '//form[@class="h5-uploader-form"]/input[@id="h5Input0"]') # 上传0
    upload_1 = (By.XPATH, '//form[@class="h5-uploader-form"]/input[@id="h5Input1"]') # 上传1

    def __init__(self, driver):
        super().__init__(driver)

    def execute_script_locator(self, locator):
        target = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", target)

    def login_s(self):
        self.open_url(html)
        self.is_click(self.username)
        self.find_element(self.username).send_keys('17521016982')
        self.is_click(self.loginPWD)
        self.find_element(self.loginPWD).send_keys('123456')
        self.is_click(self.login)
