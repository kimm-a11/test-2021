# -*-coding:utf-8-*-
from common.path import search_data

from pom.xpath.search_1_demo import SearchDemo
import pytest
from common.readyaml import ReadYaml
from assertpy import assert_that, soft_assertions
from common.base_config import html
from common.logger import logger

class TestSearch:
    @pytest.mark.demo
    @pytest.mark.parametrize('value,expect',
                             ReadYaml('filter_l.yaml', search_data)('kyt', default=True))
    def test_demo(self, driver, value, expect):
        with soft_assertions():
            search_1 = SearchDemo(driver)
            search_1.open_url(html)
            search_1.input_text(search_1.input, "baidu")
            search_1.is_click(search_1.submit_btn)
            new_url = search_1.get_current_url()
            assert_that(new_url, "error").is_not_equal_to(html)
            logger.info('{0} {1}, {2}'.format(new_url, 'df', len(new_url)))