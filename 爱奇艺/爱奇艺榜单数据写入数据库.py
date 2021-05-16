import requests
from selenium import webdriver
import time
import pymysql

class table():
    def createtable(self):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        sql1="""select director from aiyiqi"""

        query_table_sql = 'SELECT table_name FROM  information_schema.TABLES ' \
                          'WHERE table_schema = "liyixiang" AND table_name = "aiqiyi" ;'   #查询数据库表是否存在

        a = cursor.execute(query_table_sql)
        if (not a):

            sql = """create table aiqiyi(
                                director char(255) not null,actor char(255) not null,
                                introduction varchar(1000) not null,teleplay char(255) not null,remarks char(255) not null,
                                score char(255) not null,times char(255) not null,sort char(255) not null,
                                id INTEGER NOT NULL auto_increment PRIMARY KEY )"""  # 创建表语句
            cursor.execute(sql)  # 执行建表语句
    def inserts(self,s1,s2,s3,s4,s5,s6,s7,s8):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()

        sql= "insert into aiqiyi (teleplay,score,remarks,introduction,actor,director,times,sort) " \
               "values ('{}','{}','{}','{}','{}','{}','{}','{}')".\
            format(s1,s2,s3,s4,s5,s6,s7,s8)
        cursor.execute(sql)
        query_data_sql='''DELETE  from `aiqiyi`  where teleplay in (select w.teleplay from (
                            SELECT  teleplay FROM `aiqiyi` group by teleplay,times having count(teleplay)>=2 and count(times)>=2) as w)
                            and  id not in
                            (select t.minid from (SELECT  max(id) as minid FROM `aiqiyi` group by teleplay,times 
                            having count(teleplay)>=2 and count(times)>=2 ) as t)'''
        cursor.execute(query_data_sql)
        mysql.commit()

class getname():

    def geturl(self):
        self.brower.maximize_window()
        self.brower.get(self.url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.61 Safari/537.36'}
        respone = requests.get(self.url, headers=headers)
        response = requests.get(self.brower.current_url, headers=headers)
        response.encoding = response.apparent_encoding
        self.brower.find_element_by_xpath(
            "//div[@class='qy-nav-panel   qy-nav-focus']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a").click()  # 点击电视剧按钮
        self.closehandle()
        self.brower.find_element_by_xpath('//span[text()="同步热播"]/following-sibling::span[1]').click()  # 点击更多按钮
        self.closehandle()
        time.sleep(3)

    def content(self):
        i=1
        while i <= 10:
            time.sleep(2)
            target=self.brower.find_element_by_xpath("//ul[@class='qy-mod-ul']/li" + str([i])+'/div[1]/div[1]/a')
            self.brower.execute_script("arguments[0].scrollIntoView();", target)   #滚动到指定元素
            teleplay = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/a)" + str([i])).text  # 对应的影视剧名称
            # score = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/span)" + str([i])).text  # 对应的影视剧评分
            remarks = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p[2])" + str([i])).text  # 对应的影视剧备注
            time.sleep(2)
            self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/a)" + str([i])).click()  # 点击对应的影视剧
            time.sleep(2)
            windows = self.brower.window_handles  # 获取所有窗口句柄
            self.brower.switch_to.window(windows[-1])  # 切换到最新的窗口句柄
            time.sleep(2)
            introduction = self.brower.find_element_by_xpath("//div[@class='intro-right']/ul/li[3]/span/span").get_attribute(
                'innerHTML')  # 对应的影视剧简介
            actor = self.actors1()
            director=self.directors1()
            js = "window.scrollTo(100,450)"
            self.brower.execute_script(js)
            time.sleep(5)
            self.brower.find_element_by_xpath("//i[@class='qy-svgicon qy-svgicon-intro']").click()  #点击简介按钮

            try:
                self.brower.find_element_by_xpath("//a[text()='查看详情>' and @class='intro-more']").click()  #点击查看详情按钮
                self.closehandle()
            finally:
                pass

            time.sleep(3)
            try :            #获取不到评分就直接跳过
                score =self.brower.find_element_by_xpath("//i[@class='effect-score']").get_attribute(
                    'innerHTML')  # 对应的影视剧评分
                score=score.strip()  #获取到的值去空
            except:
                score = self.brower.find_element_by_xpath("//span[@class='effect-score']/i").get_attribute(
                    'innerHTML')  # 对应的影视剧评分
                score = score.strip()  # 获取到的值去空
            finally:
                pass
            self.closehandle()
            times = time.strftime('%Y_%m_%d')
            sort=i
            i=i+1
            table().inserts(teleplay,score,remarks,introduction,actor,director,times,sort)   #往数据库插入数据

    def closehandle(self):
        self.brower.close()  # 关闭当前浏览器窗口
        windows = self.brower.window_handles  # 获取所有窗口句柄
        self.brower.switch_to.window(windows[-1])  # 切换到最新的窗口句柄

    def __init__(self, url):
        self.url = url
        self.brower = webdriver.Chrome()

    def actors1(self):
        x = 1
        m = 1
        self.actors = ''

        while x == 1:

            actorss = self.brower.find_element_by_xpath(
                "//div[@class='intro-right']/ul/li[2]/span[1]/span" + str([m]) + '/a').get_attribute('title')
            m = m + 1
            try:
                self.brower.find_element_by_xpath(
                    "//div[@class='intro-right']/ul/li[2]/span[1]/span" + str([m]) + '/a')
                x = 1
            except:
                x = 0
            self.actors = self.actors + ' ' + actorss
        return self.actors

    def directors1(self):
        n = 1
        x = 1
        self.directors = ''

        while x == 1:
            directorss = self.brower.find_element_by_xpath(
                '//div[@class="intro-right"]/ul/li[1]/span/span' + str([n]) + '/a').get_attribute('title')
            n = n + 1
            try:
                self.brower.find_element_by_xpath('//div[@class="intro-right"]/ul/li[1]/span/span' + str([n]) + '/a')
                x = 1
            except:
                x = 0
            self.directors = self.directors + ' ' + directorss
        return self.directors

    def crawlings(self):
        self.geturl()
        table().createtable()
        self.content()

if __name__ == '__main__':
    url = 'https://www.iqiyi.com/'
    getname(url).crawlings()


