from selenium import webdriver
import time
import requests
import parsel
import win32api
import win32con
import win32gui
import html

browser=webdriver.Chrome()
browser.get('https://music.163.com/')
browser.maximize_window()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
#只是为了获取音乐的id所以不需要登录
# browser.find_element_by_xpath('//*[@id="auto-id-U9VG1GUwoidhPJ4W"]/a').click()#点击登录按钮
# browser.find_element_by_xpath('//*[@id="auto-id-BKehnSiu9A68MqWq"]/div/div[1]/div[2]/a').click()#点击手机号登录按钮
# browser.find_element_by_xpath('//*[@id="p"]').send_keys('17521016982')#输入手机号码
# browser.find_element_by_xpath('//*[@id="pw"]').send_keys('sharp1994')#输入密码
# browser.find_element_by_xpath('//*[@id="auto-id-EP2JgQOA1REZH9Df"]/div[1]/div[4]/label/input').click()#取消自动登录
# browser.find_element_by_xpath('//*[@id="auto-id-EP2JgQOA1REZH9Df"]/div[1]/div[5]/a').click()#点击登录按钮
#iframe=browser.find_element_by_xpath('//*[@id="g_iframe"]') #查看框架
browser.switch_to.frame('contentFrame')#选择框架
target = browser.find_element_by_xpath("(//a[text()='更多'])[3]")
browser.execute_script("arguments[0].scrollIntoView();", target)
browser.find_element_by_xpath("(//a[text()='更多'])[3]").click()   #点击榜单的更多按钮
browser.find_element_by_xpath('//*[@id="toplist"]/div[1]/div/ul[1]/li[1]/div/p[1]/a').click()   #点击榜单的第一个排行榜
url=browser.current_url #获取当前页面url
response = requests.get(url, headers=headers) #响应的内容
response.encoding = response.apparent_encoding  #内容编码
# contents=sel.xpath("//table[@class='m-table m-table-rank']/tbody").extract()   #将响应的内容按照xpath保存
# contents2 = []
# for content in contents:
#     contents2.append(content.strip())
# with open('网易云' + '.txt', mode='a+', encoding='utf-8') as f:
#     f.write("\n".join(contents2))
i=1
while i<=3:  #榜单只爬取100首
    m='tr'+'{}'.format([i])
    time.sleep(1)
    ele=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[2]/div[1]/div/span".format(m)) #将内容按照xpath保存
    time.sleep(1)
    gqid=ele.get_attribute("data-res-id") #获取对应歌曲唯一的id的值
    time.sleep(1)
    name=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[2]/div[1]/div/div/span/a/b".format(m)).text  #获取歌曲名称html.unescape(name)
    name = name.split(';')
    name = str(name)
    name=name.replace(r'\n','').replace('IMW','')
    name=name.strip('[]')
    name = str(name)
    name=name.strip("''")
    author=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[4]/div".format(m)).text  #获取歌手名称
    # browser.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(gqid))     #生成榜单的链接
    # handles = browser.window_handles #切换窗口
    # browser.switch_to.window(handles[-1])  #切换窗口
    fo=requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(gqid)).content
    data = requests.get("http://music.163.com/song/media/outer/url?id={}.mp3'".format(gqid),headers, stream=True)
    synth_file = 'D:'+'\music'+'\{}'.format(name)+ ".mp3"
    with open(synth_file, mode='a+') as f:
        f.write(str(fo))
        print(name +'.mp3'+'写出完毕!')
    #browser.get('/html/body/video').click() #鼠标点击图标位置
    # win32api.keybd_event(0x11,0x53)  #模拟键盘按ctrl+S
    i=i+1
browser.quit()
