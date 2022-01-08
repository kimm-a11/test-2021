from common.readconfig import ReadConfigYaml
from common.path import *

html = ReadConfigYaml('config.yaml', config)('html')
Timeout = ReadConfigYaml('config.yaml', config)('Timeout')


