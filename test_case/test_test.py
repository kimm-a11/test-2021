import pytest
import requests
#这是pytest的数据驱动,indeirect=True是把login_r当作函数去执行
#从下往上执行
#两个数据进行组合测试，有3*3个测试用例执行(test_user_data1的个数*test_user_data2的个数
def test_login(self,driver):
    url = 'https://shuliecloud.com/login'
    log_data = {'username': 17521016982, 'password': 123456}
    headers= 'application/x-www-form-urlencoded; charset=UTF-8'
    data = requests.post(
        url=url, json=log_data,headers=headers
        )
    print(data)


    # payload={}
    # files=[
    #   ('$file',('icudtl.dat',open('/D:/Postman/Postman/app-7.36.7/icudtl.dat','rb'),'application/octet-stream'))
    # ]
    # headers = {}
    #
    # response = requests.request("PUT", url, headers=headers, data=payload, files=files)