import sys
from os.path import *
import os

# 框架原本的位置路径
curl_path = dirname(dirname(realpath(__file__)))
# common 路径
common = os.path.join(curl_path, 'common')

# 测试数据存放的位置
data = os.path.join(curl_path, 'data')

# 测试数据search存放的位置

search_data = os.path.join(data, 'search')

# chromedriver.exe存放的位置

chromedriver = os.path.join(curl_path, 'driver')

# config存放的位置

config = os.path.join(curl_path, 'config')

# log存放的位置

log = os.path.join(curl_path, 'log')

