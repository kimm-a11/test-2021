# -*-coding:utf-8-*-
import allure

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
        # with allure.step("测试步骤"):
        #     with soft_assertions():
        #         search_1 = SearchDemo(driver)
        #         search_1.open_url(html)
        #         # assert_that(1, "error").is_equal_to(2)
        #         search_1.input_text(search_1.input, "baidu")
        #         search_1.find_element(search_1.submit_btn)
        #         text = search_1.get_css_value(search_1.submit_btn, 'value')
        #         print(text)
        #         search_1.is_click(search_1.submit_btn)
        #         new_url = search_1.get_current_url()
        #         text_1 = search_1.is_element_text(search_1.all_page)
        #         print(text_1)
        #         # assert_that(new_url, "error").is_not_equal_to(html)
        #         assert_that(new_url, "error").is_not_equal_to(html)
                dat= [33,44,55,33]
                a=3
                dat.count(33)
                print(dat.insert(4,7))

