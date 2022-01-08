# #-*-coding:utf-8-*-
import os
import unittest
# from HTMLTestRunner import HTMLTestRunner
from send_mail import Mail


if __name__ == '__main__':

    # 被测试基本的路径
    test_dir = os.path.join(os.getcwd(), "./")
    # pattern脚本名称匹配规则
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # 存放测试报告的文件夹
    report_dir = './test_report'
    report = report_dir + '/' + 'report.html'
    # 打开文件再报告文件写入测试结果
    # with open(report, 'wb') as f:
    #     runner = HTMLTestRunner(stream=f, title='Test Report', description='Test Case Result')
    #     runner.run(discover)

    # 定义邮件参数内容
    msg = '测试报告已生成,请注意查收'   # 邮件正文
    title = '《测试报告》'    # 邮件标题
    receivers = ['邮件接收者地址']   # 邮件接收者
    attachment = [r"D:\Pycharm\PycharmProjects\NewProject\wingtosapce\testcase\test_report\report.html"]

    # 通过邮件发送最新的报告
    Mail().sendmail(receivers, title, msg, attachment)

