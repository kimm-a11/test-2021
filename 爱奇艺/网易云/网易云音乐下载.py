from selenium import webdriver
import time
import requests
import html
browser=webdriver.Chrome()
browser.get('https://music.163.com/')
browser.maximize_window()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
browser.switch_to.frame('contentFrame')#选择框架
target = browser.find_element_by_xpath("(//a[text()='更多'])[3]")
browser.execute_script("arguments[0].scrollIntoView();", target)
browser.find_element_by_xpath("(//a[text()='更多'])[3]").click()   #点击榜单的更多按钮
browser.find_element_by_xpath('//*[@id="toplist"]/div[1]/div/ul[1]/li[1]/div/p[1]/a').click()   #点击榜单的第一个排行榜
url=browser.current_url #获取当前页面url
response = requests.get(url, headers=headers) #响应的内容
response.encoding = response.apparent_encoding  #内容编码
i=1
while i<=3:  #榜单只爬取100首
    m='tr'+'{}'.format([i])
    time.sleep(1)
    ele=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[2]/div[1]/div/span".format(m)) #将内容按照xpath保存
    time.sleep(1)
    gqid=ele.get_attribute("data-res-id") #获取对应歌曲唯一的id的值
    time.sleep(1)
    name=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[2]/div[1]/div/div/span/a/b".format(m))  #获取歌曲名称html.unescape(name)
    name =name.get_attribute('title') #获取歌曲名称html.unescape(name)
    author=browser.find_element_by_xpath("//table[@class='m-table m-table-rank']/tbody/{}/td[4]/div".format(m)).text  #获取歌手名称
    fo=requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(gqid)).content
    data = requests.get("http://music.163.com/song/media/outer/url?id={}.mp3'".format(gqid),headers, stream=True)
    synth_file = 'D:'+'\music'+'\{}'.format(name)+ ".mp3"
    with open(synth_file, mode='a+') as f:
        f.write(str(fo))
        print(name +'.mp3'+'写出完毕!')
    i=i+1
browser.quit()