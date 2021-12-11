import yaml
from common.path import search_data
import os
import string


class ReadYaml:
    def __init__(self, name: str, path):
        yaml1 = os.path.join(path, name)
        # data1 = open(yaml1)
        with open(yaml1, encoding="utf-8") as f:
            self.d1 = yaml.safe_load(f)

    def __getitem__(self, key):
        return self.d1[key]

    def __call__(self, key, index=0, expect='expect', default=False):
        need_data = self[key]
        first_arg = need_data[index]
        template = string.Template(first_arg)
        need_data.remove(first_arg)
        if default:
            return [(template.safe_substitute(**value), value[expect]) for value in need_data]
        return [template.safe_substitute(**data) for data in need_data]


if __name__ == "__main__":
    print(ReadYaml('filter_l.yaml', search_data)('kyt'))
pass
