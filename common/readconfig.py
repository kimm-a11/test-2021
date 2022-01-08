import yaml
from common.path import search_data
import os
import string

class ReadConfigYaml:
    def __init__(self, name: str, path):
        yaml1 = os.path.join(path, name)
        # data1 = open(yaml1)
        with open(yaml1, encoding="utf-8") as f:
            self.d1 = yaml.safe_load(f)

    def __getitem__(self, key):
        return self.d1[key]

    def __call__(self, key):
        return self[key]


if __name__ == "__main__":
    print(ReadConfigYaml('filter_l.yaml', search_data)('kyt'))
pass
