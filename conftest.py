import pytest
from common.path import chromedriver
from selenium.webdriver.remote import webdriver
from selenium import webdriver

@pytest.fixture(scope="function")
def driver(request):
    global driver
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    # driver.get(
    #     'https://blog.csdn.net/lmseo5hy/article/details/81704426?spm=1001.2101.3001.6661.1&utm_medium=distribute'
    #     '.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.fixedcolumn&depth_1-utm_source=distribute'
    #     '.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.fixedcolumn')

    def close():
        driver.quit()

    request.addfinalizer(close)
    return driver


