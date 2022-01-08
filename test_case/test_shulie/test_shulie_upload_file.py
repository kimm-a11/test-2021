# #-*-coding:utf-8-*-

from common.path import search_data

from pom.xpath.search_1_demo import SearchDemo
import pytest
from common.readyaml import ReadYaml
from assertpy import assert_that, soft_assertions
from common.base_config import html


class TestSearch:
    @pytest.mark.demo
    @pytest.mark.parametrize('value,expect',
                             ReadYaml('filter_l.yaml', search_data)('kyt', default=True))
    def test_demo(self, driver, value, expect):
        with soft_assertions():
            search_1 = SearchDemo(driver)
            search_1.login_s()
