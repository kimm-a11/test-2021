import pytest
import os
import allure
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


