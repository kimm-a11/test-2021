# #-*-coding:utf-8-*-
import yagmail
import time


class Mail:
    """
    邮件相关类
    """

    def log(self, content):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'{now_time}: {content}')

    def sendmail(self, receivers, title, msg,attachment):
        """
        发送邮件

        Arguments:
            msg {str} -- 邮件正文
            title {str} -- 邮件标题
            receivers {list} -- 邮件发送者，数组
            attachment -- 测试报告附件
        """

        yag = yagmail.SMTP(
            host='smtp.qq.com', user='2598614627@qq.com',
            password='iplpvzuzgtrlecdg', smtp_ssl=True
        )

        try:
            # yag.send(receivers, title, msg)

            yag.send(receivers, title, msg, attachment)
            self.log("邮件发送成功")

        except BaseException as e:
            print(e)
            self.log("Error: 无法发送邮件")
