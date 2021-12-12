# #-*-coding:utf-8-*-
import pymysql

from selenium import webdriver
import time
import pymysql
import requests


class TestTable:  # 表
    def create_table(self, ip, table_name, name="root", sql="mysql", sql_name="liyixiang"):
        mysql = pymysql.connect(ip, name, sql, sql_name)
        cursor = mysql.cursor()
        query_table_sql = "SELECT table_name FROM  information_schema.TABLES ' \
                          'WHERE table_schema = '{}' AND table_name = '{}' ;".format(sql_name, table_name)  # 查询数据库表是否存在
        a = cursor.execute(query_table_sql)
        if (not a):
            sql_create = """create table '{}'(
                                playid char(255) not null,title char(255) not null,
                                singer char(255) not null,album char(255) not null,mvid char(255),
                                duration char(255) not null,update_time DATETIME not null,
                                id INTEGER NOT NULL auto_increment PRIMARY KEY  )""".format(table_name)  # 创建表语句
            cursor.execute(sql_create)  # 执行建表语句

    def insert_data(self, s1, s2, s3, s4, s5, s6, s7, ip, table_name, name="root", sql="mysql", sql_name="liyixiang"):
        mysql = pymysql.connect(ip, name, sql, sql_name)
        cursor = mysql.cursor()
        sql_insert = "insert into '{}' (playid,title,singer,album,mvid,duration,update_time) " \
                     "values ('{}','{}','{}','{}','{}','{}','{}')". \
            format(table_name, s1, s2, s3, s4, s5, s6, s7)
        cursor.execute(sql_insert)
        mysql.commit()
        delete_data_sql = '''delete from `{}`  where playid in (select w.playid from (SELECT  playid FROM `wangyiyun` group by playid,mvid 
                           having count(playid)>=2 and count(mvid)>=2) as w)and  id not in 
                           (select t.minid from (SELECT  max(id) as minid FROM `wangyiyun` 
                         group by playid,mvid having count(playid)>=2 and count(mvid)>=2 ) as t)'''.format(table_name)
        cursor.execute(delete_data_sql)
        mysql.commit()

    def search_query(self, s1, s5, ip, table_name, name="root", sql="mysql", sql_name="liyixiang"):
        mysql = pymysql.connect(ip, name, sql, sql_name)
        cursor = mysql.cursor()
        query_data_sql = "select title from {} where title like '%{}%' or singer like '%{}%'".format(table_name, s1, s5)
        try:
            cursor.execute(query_data_sql)
            # 获取所有记录列表
            self.query_data = cursor.fetchall()
        except (Exception, Exception) as e:
            print(type(e), e)
            print("没有查询到数据")
        return self.query_data

    def input_data(self, playid, title, singer, album, duration, update_time, mvid,ip, table_name, name="root", sql="mysql", sql_name="liyixiang"):  # 将数据插入数据库
        self.create_table(ip, table_name, name="root", sql="mysql", sql_name="liyixiang")
        self.insert_data(playid, title, singer, album, mvid, duration, update_time,ip, table_name, name="root", sql="mysql", sql_name="liyixiang")
