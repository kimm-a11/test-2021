from time import sleep

import requests as requests
from bs4 import BeautifulSoup
from chardet import detect
from selenium import webdriver
from urllib import request


class Item():
    name = ''
    id = ''


class GetMusic():

    def get_respond_content(self): #返回url数据
        url = 'https://music.163.com/discover/toplist'
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        respond = request.Request(url,headers=header)
        respond = request.urlopen(respond).read()
        char = detect(respond)['encoding']
        page_info = respond.decode(char)
        return page_info

    def get_music_info(self):
        music_info = []
        page = self.get_respond_content()
        pageInfo = Beautifuget_respond_contentlSoup(page, 'lxml')
        music_lists = pageInfo.find('ul','f-hide').find_all('li')

        for music_list in music_lists:
            music_item = Item()
            music_item.name = music_list.find('a').text
            music_item.id = music_list.find('a').get('href').replace(r'/song?id=','')
            music_info.append(music_item)

        return music_info

    def download_music(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        musics = self.get_music_info()
        for music in musics:
            song = requests.get("http://music.163.com/song/media/outer/url?id={}.mp3'".format(music.id), headers=header,stream=True).content
            song_path = './' + music.name + ".mp3"
            with open(song_path, mode='wb') as f:
                f.write(song)
                print(music.name + '.mp3' + '保存成功!')

if __name__ == '__main__':
    GetMusic().download_music()

