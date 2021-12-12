import pytest
from common.path import search_data

from common.readyaml import ReadYaml


@pytest.mark.parametrize('value,expect', ReadYaml('filter_l.yaml', search_data)('kyt',default=True))
def test_test(driver,value,expect):
    print(ReadYaml('filter_l.yaml', search_data)('kyt',default=True))
    str=[1,2,3,4,5,2,6]
    str.pop(2)
    print(str)
    assert 1==2