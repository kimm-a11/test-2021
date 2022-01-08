# #-*-coding:utf-8-*-
from common.send_mail import Mail
import pytest
from common.readyaml import ReadYaml
from common.path import search_data
from pom.xpath.search_1_demo import SearchDemo


class TestLogin:
    @pytest.mark.demo
    @pytest.mark.parametrize('value,expect',
                             ReadYaml('filter_l.yaml', search_data)('kyt', default=True))
    def test_demo(self, driver, value, expect):
        search_1 = SearchDemo(driver)
        search_1.login_s()
        attachment=r'D:\PycharmProjects\python_demo\report\cef1a39e-2524-4296-b0c7-bca100fc6b04-attachment.png'
        Mail().sendmail(['2598614627@qq.com'],
            '服务挂了', '测试',attachment)
