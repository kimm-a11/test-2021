import pytest
import os
import allure
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    global drivers
    option = webdriver.ChromeOptions()
    drivers = webdriver.Chrome(options=option)

    # driver.get(
    #     'https://blog.csdn.net/lmseo5hy/article/details/81704426?spm=1001.2101.3001.6661.1&utm_medium=distribute'
    #     '.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.fixedcolumn&depth_1-utm_source=distribute'
    #     '.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.fixedcolumn')

    def close():
        drivers.quit()
    request.addfinalizer(close)
    return drivers


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    """
    hook pytest失败
    :param item:
    :param call:
    :return:
    """

    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # mode = "a" if os.path.exists("failures") else "w"
        # with open("failures", mode) as f:
        #     if "tmpdir" in item.fixturenames:
        #         extra = " (%s)" % item.funcargs["tmpdir"]
        #     else:
        #         extra = ""
        #     f.write(rep.nodeid + extra + "\n")
        with allure.step('添加失败截图...'):
            allure.attach(drivers.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# @pytest.fixture
# def amdont(self):


