# -*- coding: utf-8 -*-

import  tkinter
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
            cursor.execute(sql)  # 执行建表语句


    def inserts(self,s1,s2,s3,s4,s5,s6,s7):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        sql="insert into wangyiyun (playid, title, singer, album, duration, update_time, mvid) values ('{}','{}','{}','{}','{}','{}','{}')".\
            format(s1,s2,s3,s4,s5,s6,s7)
        time.sleep(1)
        cursor.execute(sql)
        mysql.commit()
        delete_data_sql='''delete from `wangyiyun`  where playid in (select w.playid from (SELECT  playid FROM `wangyiyun` group by playid,mvid 
                           having count(playid)>=2 and count(mvid)>=2) as w)and  id not in 
                           (select t.minid from (SELECT  max(id) as minid FROM `wangyiyun` 
                         group by playid,mvid having count(playid)>=2 and count(mvid)>=2 ) as t)'''
        cursor.execute(delete_data_sql)
        mysql.commit()


    def query(self,s10):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        query_data_show = "select title,singer,album,duration  from wangyiyun where title like '%{}%' or singer like '%{}%' ".format(s10,s10)
        query_data_playlink="select playid from  wangyiyun where title like '%{}%' or singer like '%{}%'".format(s10,s10)
        query_data_sql_mvlink="select mvid from  wangyiyun where title like '%{}%' or singer like '%{}%'".format(s10,s10)
        try:
            cursor.execute(query_data_show)
            self.query_data_show = cursor.fetchall()
        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")
        try:
            cursor.execute(query_data_playlink)
            self.playlink = cursor.fetchall()
        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")
        try:
            cursor.execute(query_data_sql_mvlink)
            self.mvlink = cursor.fetchall()
            # 获取所有记录列表
        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")


        return self.query_data_show,self.playlink,self.mvlink

    def path(self,s10):
        mysql = pymysql.connect("192.170.3.3", "root", "mysql", "liyixiang")
        cursor = mysql.cursor()
        query_data_count="select count(* ) from wangyiyun where title like '%{}%' or singer like '%{}%' ".format(s10,s10)
        try:
            cursor.execute(query_data_count)
            self.query_data_count = cursor.fetchall()
            for list in self.query_data_count:
                self.query_data_count=self.query_data_count[0]
                self.query_data_count=str(self.query_data_count).strip('()').strip(',')
                if self.query_data_count=='0':
                    self.path=0
                else :
                    self.path = 1

        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")
        return self.path


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
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/81.0.4044.129 Safari/537.36'}
        respone = requests.get(self.url, headers=headers)
        response.encoding = response.apparent_encoding
        self.browser.switch_to.frame('g_iframe')
        self.browser.find_element_by_xpath('//*[@id="m-search-input"]').send_keys('{}'.format(s10))#   网易云输入框
        self.browser.find_element_by_xpath("//a[@class='btn j-flag']").click()  #点击查询按钮
        time.sleep(2)
        self.browser.find_element_by_xpath("//em[text()='单曲']").click()   #点击单曲按钮
        time.sleep(2)


    def getsongnames(self, x1):   #获取到网易云页面的值
        self.enter_wangyi(x1)
        i=1
        getsongname_x = 1
        while getsongname_x==1:
            try:
                playid = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[2]/div[1]/div[1]/a[1]").get_attribute('href')
                # 获取歌曲的song_title
                title = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[2]/div[1]/div[1]/a[1]/b").get_attribute('title')
                # 获取歌曲的songp_singger
                try:
                    singer = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[4]/div[1]/a/span").get_attribute('innerHTML')
                except:

                    singer = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[4]/div[1]/a").get_attribute('innerHTML')
                # else:
                #
                #     singer = self.browser.find_element_by_xpath(
                #         "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                #         + str([i]) + "/div[4]/div[1]").get_attribute('innerHTML')
                #     # 获取歌曲的songp_album
                album = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[5]/div[1]/a").get_attribute('title')
                # 获取歌曲的songp_time
                duration = self.browser.find_element_by_xpath(
                    "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                    + str([i]) + "/div[6]").get_attribute('innerHTML')
                update_time = time.strftime('%Y_%m_%d %H_%M_%S')
                try:
                    mvid = self.browser.find_element_by_xpath(
                        "//ul[@class='m-tabs m-tabs-srch f-cb ztag']/following-sibling::div[1]/div[1]/div[1]/div"
                        + str([i]) + "/div[2]/div[1]/div[1]/a[2]").get_attribute('href')
                    print(mvid)
                except:
                    mvid = 'null'
                i = i + 1
                getsongname_x = 1
            except:
                try:
                    self.browser.find_element_by_xpath("//a[contains(@class,'js-disabled')][text()='下一页']")
                    getsongname_x = 0
                except :
                    target = self.browser.find_element_by_xpath("//a[text()='工业和信息化部备案管理系统网站']")
                    self.browser.execute_script("arguments[0].scrollIntoView();", target)  # 滚动到指定元
                    self.browser.find_element_by_xpath("//a[text()='下一页']").click()
                    i = 1
                    time.sleep(2)
                    getsongname_x = 1
            table().createtable_wangyiyun()
            table().inserts(playid, title, singer, album, duration, update_time, mvid)

class CanvasDemo:
    def __init__(self):
        self.master = tkinter.Tk() #创建窗口
        self.search_text = tkinter.StringVar()
        self.inputdata = ''


    def Canvas(self):
        #c窗口名称
        self.master.title("网易云音乐下载")
        scrollbar = tkinter.Scrollbar(self.master,orient=tkinter.VERTICAL).place(x = 800,width=20,height=1000)

        #输入框头部显示
        tkinter.Label(self.master,text='歌曲名称:',font='Times',bg='white').grid(row=3,column=0)#
        tkinter.Entry(self.master,textvariable = self.search_text).grid(row=3,column=1)  #歌曲名称输入框
        self.search_text.set("")

        tkinter.Button(self.master,text='查找',command=self.onclick).grid(row=3,column=2)   #点击查找按钮

        #显示列
        tkinter.Label(self.master,text='歌曲播放',font='Times',bg='white').grid(row=4,column=0)#
        tkinter.Label(self.master,text='歌曲名称',font='Times',bg='white').grid(row=4,column=1)#
        tkinter.Label(self.master,text='演唱者',font='Times',bg='white').grid(row=4,column=2)#
        tkinter.Label(self.master,text='专辑',font='Times',bg='white').grid(row=4,column=3)#
        tkinter.Label(self.master,text='时长',font='Times',bg='white').grid(row=4,column=4)#
        tkinter.Label(self.master,text='音乐下载',font='Times',bg='white').grid(row=4,column=5)#
        tkinter.Button(self.master,text='播放')


        tkinter.mainloop()

    def onclick(self):
        self.inputdata=self.search_text.get()
        path=table().path(self.inputdata)
        if path==0:
            wangyiyun_getdata(url).getsongnames(self.inputdata)
        self.showinfo(self.inputdata)


    def showinfo(self,x):
        show_data_show=table().query(self.inputdata)[0]
        playlink = table().query(self.inputdata)[1]
        mvlink=table().query(self.inputdata)[2]
        g,p=0,5
        for  list in show_data_show:
            tkinter.Label(self.master, text=show_data_show[g]).grid(row=p, column=1)
            tkinter.Button(self.master, text='播放',command=self.playmusic).grid(row=p, column=0)  # 点击播放按钮
            playlinks = str(playlink[g])
            self.playlinks = playlinks.strip('()').strip(',').strip("''")
            mvlinks = str(mvlink[g])
            self.mvlinks = mvlinks.strip('()').strip(',').strip("''")
            if self.mvlinks != 'null':
                tkinter.Button(self.master, text='MV', command=self.mv).grid(row=p, column=2)  # 点击播放按钮
            g=g+1
            p=p+1
        return self.playlinks,self.mvlinks
    def playmusic(self):
        browser = webdriver.Chrome()
        browser.get(self.playlinks)
    def mv(self):
        browser = webdriver.Chrome()
        browser.get(self.mvlinks)

if __name__=='__main__':
    url='https://music.163.com/#/search'
    CanvasDemo().Canvas()
