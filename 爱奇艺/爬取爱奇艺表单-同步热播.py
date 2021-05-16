import requests
from selenium import webdriver
import  parsel
import time
import xlwt

class Item():
    director='' #导演
    actor=''#主演
    introduction=''#简介
    teleplay=''#电视剧名称
    remarks='' #备注
    score=''#评分
    times='' #爬取的时间

class getname():
    def geturl(self):
        # self.brower = webdriver.PhantomJS()
        # self.brower = webdriver.Chrome()
        self.brower.maximize_window()
        self.brower.get(self.url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
        respone = requests.get('https://www.iqiyi.com/', headers=headers)
        response = requests.get(self.brower.current_url, headers=headers)
        response.encoding = response.apparent_encoding
        self.brower.find_element_by_xpath(
            "//div[@class='qy-nav-panel   qy-nav-focus']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a").click()  # 点击电视剧按钮
        self.brower.close()  # 关闭当前浏览器窗口
        windows = self.brower.window_handles  # 获取所有窗口句柄
        self.brower.switch_to.window(windows[-1])  # 切换到最新的窗口句柄

    def __init__(self, url):
        self.url = url
        self.brower = webdriver.Chrome()

    def getnames(self):
        url=self.geturl()
        items=[]
        i = 1
        while i <= 2:
            item=Item()
            item.teleplay = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/a)" + str([i])).text  # 对应的影视剧名称
            item.score = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/span)" + str([i])).text  # 对应的影视剧评分
            item.remarks = self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p[2])" + str([i])).text  # 对应的影视剧备注
            self.brower.find_element_by_xpath("(//div[@class='title-wrap']/p/a)" + str([i])).click()  # 点击对应的影视剧
            time.sleep(2)
            windows = self.brower.window_handles  # 获取所有窗口句柄
            self.brower.switch_to.window(windows[-1])  # 切换到最新的窗口句柄

            item.introduction = self.brower.find_element_by_xpath("//div[@class='intro-right']/ul/li[3]/span/span").get_attribute(
                'innerHTML')  # 对应的影视剧简介
            x=1
            m = 1
            actors = ''
            while x==1:

                actorss=self.brower.find_element_by_xpath(
                    "//div[@class='intro-right']/ul/li[2]/span[1]/span"+str([m])+'/a').get_attribute('title')
                m=m+1
                try :
                    self.brower.find_element_by_xpath(
                    "//div[@class='intro-right']/ul/li[2]/span[1]/span"+str([m])+'/a')
                    x=1
                except:
                    x=0
                actors=actors+' '+actorss
            item.actor=actors
            n = 1
            x = 1
            directors = ''
            while x==1:
                directorss=self.brower.find_element_by_xpath('//div[@class="intro-right"]/ul/li[1]/span/span'+str([n])+'/a').get_attribute('title')
                n=n+1
                try :
                    self.brower.find_element_by_xpath('//div[@class="intro-right"]/ul/li[1]/span/span'+str([n])+'/a')
                    x=1
                except:
                    x=0
                directors=directors+' '+directorss
            item.director=directors
            now = time.strftime('%Y_%m_%d')
            item.times=now
            self.brower.close()  # 关闭当前浏览器窗口
            windows = self.brower.window_handles  # 获取所有窗口句柄
            self.brower.switch_to.window(windows[-1])  # 切换到最新的窗口句柄
            items.append(item)
            i = i + 1
        return items

    def writeex(self):
            items=self.getnames()
            book = xlwt.Workbook(encoding='utf-8', style_compression=0)
            sheet = book.add_sheet('st', cell_overwrite_ok=True)
            q= 1
            sheet.write(0, 0, '排行')
            sheet.write(0, 1, '电视剧名称')
            sheet.write(0, 2, '导演')
            sheet.write(0, 3, '主演')
            sheet.write(0, 4, '备注')
            sheet.write(0, 5, '评分')
            sheet.write(0, 6, '简介')
            sheet.write(0, 7, '爬取时间')

            for item in items:
                sheet.write(q, 0, q)
                sheet.write(q, 1, item.teleplay)
                sheet.write(q, 2, item.director)
                sheet.write(q, 3, item.actor)
                sheet.write(q, 4, item.remarks)
                sheet.write(q, 5, item.score)
                sheet.write(q, 6, item.introduction)
                sheet.write(q, 7, item.times)
                q=q+1
            now = time.strftime('%Y_%m_%d %H_%M_%S')
            filename = './' +now+ 'spider163.xls'
            book.save(filename)



if __name__ == '__main__':
    url = 'https://www.iqiyi.com/'
    getname(url).writeex()

