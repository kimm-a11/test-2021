from selenium import webdriver
import time
import pymysql
import requests
class table():   #表
    def createtable_wangyiyun(self):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        query_table_sql = 'SELECT table_name FROM  information_schema.TABLES ' \
                          'WHERE table_schema = "liyixiang" AND table_name = "wangyiyun" ;'   #查询数据库表是否存在
        a = cursor.execute(query_table_sql)
        if (not a):
            sql = """create table wangyiyun(
                                playid char(255) not null,title char(255) not null,
                                singer char(255) not null,album char(255) not null,mvid char(255),
                                duration char(255) not null,update_time DATETIME not null,
                                id INTEGER NOT NULL auto_increment PRIMARY KEY  )"""  # 创建表语句
            self.cursor.execute(sql)  # 执行建表语句

    def inserts(self,s1,s2,s3,s4,s5,s6,s7):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        sql="insert into wangyiyun (playid,title,singer,album,mvid,duration,update_time) " \
               "values ('{}','{}','{}','{}','{}','{}','{}')".\
            format(s1,s2,s3,s4,s5,s6,s7)
        cursor.execute(sql)
        mysql.commit()
        delete_data_sql='''delete from `wangyiyun`  where playid in (select w.playid from (SELECT  playid FROM `wangyiyun` group by playid,mvid 
                           having count(playid)>=2 and count(mvid)>=2) as w)and  id not in 
                           (select t.minid from (SELECT  max(id) as minid FROM `wangyiyun` 
                         group by playid,mvid having count(playid)>=2 and count(mvid)>=2 ) as t)'''
        cursor.execute(delete_data_sql)
        mysql.commit()
    def qyery(self,s1,s5):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        query_data_sql = "select title from wangyiyun where title like '%{}%' or singer like '%{}%'".format(s1, s5)
        try:
            cursor.execute(query_data_sql)
            # 获取所有记录列表
            self.query_data = cursor.fetchall()
        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")
        return self.query_data
class showdata():
    def showdata(self,query_data):
        r=1
        for playid,title,singer,album,mvid,duration,update_time in self.query_data:
            playid, title, singer, album, mvid, duration, update_time=self.query_data[r]
            r=r+1
class wangyiyun_getdata():   #获取网易数据并且插入数据库
    def __init__(self,url):
        self.url=url
        self.browser = webdriver.Chrome()


    def enter_wangyi(self,s10):
        self.browser.get(self.url)
        self.browser.maximize_window()
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/81.0.4044.129 Safari/537.36'}
        respone = requests.get(self.url, headers=headers)
        response = requests.get(self.browser.current_url, headers=headers)
        response.encoding = response.apparent_encoding
        self.browser.switch_to.frame('g_iframe')
        self.browser.find_element_by_xpath('//*[@id="m-search-input"]').send_keys('{}'.format(s10)) #调取弹窗的值输入网易云输入框
        self.browser.find_element_by_xpath("//a[@class='btn j-flag']").click()  #点击查询按钮
        time.sleep(2)
        self.browser.find_element_by_xpath("//em[text()='单曲']").click()   #点击单曲按钮
        time.sleep(2)



    def getsongnames(self):   #获取到网易云页面的值
        i=1
        getsongname_x=1
        while getsongname_x==1:
            try:
                self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[2]/div[1]/div[1]/a[1]")
                getsongname_x = 1
            except:
                getsongname_x = 0
            if getsongname_x==1:
                playids = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[2]/div[1]/div[1]/a[1]").get_attribute('href')
                self.playid = 'https://music.163.com/' + playids
                # 获取歌曲的song_title
                self.title = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[2]/div[1]/div[1]/a[1]/b").get_attribute('title')
                # 获取歌曲的songp_singger
                try:
                    self.singer = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[4]/div[1]/a/span").get_attribute('innerHTML')
                except:
                    self.singer = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[4]/div[1]/a").get_attribute('innerHTML')
                else:
                    self.singer = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[4]/div[1]").get_attribute('innerHTML')
                # 获取歌曲的songp_album
                self.album = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[5]/div[1]/a").get_attribute('title')
                # 获取歌曲的songp_time
                self.duration = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[6]").get_attribute('innerHTML')
                self.update_time = time.strftime('%Y_%m_%d %H_%M_%S')
                try:
                    mvids=self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[2]/div[1]/div[1]/a[2]")
                    self.mvid = 'https://music.163.com/' + mvids
                except:
                    self.mvid='null'
                    i=i+1
                print(self.title)
            else:
                target = self.browser.find_element_by_xpath("//a[text()='工业和信息化部备案管理系统网站']")
                self.browser.execute_script("arguments[0].scrollIntoView();", target)  # 滚动到指定元y:
                # js = "window.scrollTo(100,450)"
                # self.browser.execute_script(js)
                try:
                    self.browser.find_element_by_xpath("//a[text()='下一页']").click()
                    i=1
                    time.sleep(2)
                except (Exception,Exception) as e:
                    pass
                    # print(type(e),e)
                    # print("页面没有下一页按钮可点击")
            # print("getsongname_x:"+str(getsongname_x))
        return self.playid, self.title, self.singer, self.album, self.duration, self.update_time,self.mvid

    def input_data(self):   #将数据插入数据库
            playid,title,singer,album,duration,update_time,mvid=self.getsongnames()
            table().createtable_wangyiyun()
            table().inserts(playid,title,singer,album,mvid,duration,update_time)
    def crawling(self):   #执行脚本
        self.enter_wangyi(self.inputsongname_input)
        self.input_data()
if __name__=='__main__':
    url='https://music.163.com/#/search'
    wangyiyun_getdata(url).crawling()
