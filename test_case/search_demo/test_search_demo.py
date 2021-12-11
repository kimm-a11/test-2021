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
            search_1.open_url(html)
            text_blog = search_1.is_element_text(search_1.login)
            print(text_blog)
            search_1.execute_script_locator(search_1.login)
            search_1.is_click(search_1.login)
            assert_that(value, "runner").is_equal_to(expect)
            print(search_1.get_current_url())
