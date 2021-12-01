import bs4, time, selenium, requests, json, schedule, csv, os, urllib, urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import pandas as pd
import numpy as np
from urllib.parse import quote_plus
from urllib.request import urlopen
from datetime import date, time, datetime

mountain_data = pd.read_csv('/home/rapa/Documents/mountain/mtngps.csv', encoding='utf-8')
mnt_data = pd.read_csv('/home/rapa/Documents/mountain/mountain1.csv', encoding='utf-8')
db_url='mongodb://127.0.0.1:27017'
headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
list_data = []
img_data = []
k = 0
i = 0
data_mnt = []

try:
    MongoClient(db_url)['mountain'].sampleCollection.drop()
except:
    pass

for k in range(0, 199):
    if k % 2 == 0:
        datas = pd.DataFrame(mnt_data, index=[k])
        mnt_datas = str(datas['C_info'][k]).replace('\xa0', '', 100).replace('\n','',100)
        data_mnt.append(mnt_datas)    
for i in range(0, 100):
    try:
        list_data.clear()
        img_data.clear()
        soup1.clear()
        soup2.clear()
    except:
        pass
    mountain_datas = pd.DataFrame(mountain_data, index=[i])
    class_ = str(mountain_datas['C_name']).replace('\nName: C_name', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    address_ = str(mountain_datas['C_gps']).replace('\nName: C_gps', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    address_ = address_.split(',')
    address_1 = address_[0]
    address_2 = address_[1]
    C_ad = str(mountain_datas['C_ad']).replace('\nName: C_ad', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    # try:
    #     if class_[-1]= ')':
    # except:
        # pass
    
    url1 = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={class_}'
    url2 = f'https://www.google.com/search?q={C_ad} 기상정보'
################################################################################################################  
    # url = f'http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI?serviceKey=0c%2BeEdG%2Fbkm34OVKN%2BIMu9QP0kI1eNbPqitvIGQz15VBbq1nM8BJEcdPZqWZGSsqNLzEWe0R4qJnHqmmDEQHjA%3D%3D&searchWrd={class_}'
################################################################################################################  
    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # data = soup.find_all('item')

    # for item in data:
    #     mntiname = item.find('mntiname').get_text()
    #     mntiadd = item.find('mntiadd').get_text()
    #     mntidetails = item.find('mntidetails').get_text()
    #     mntilistno = item.find('mntilistno').get_text()
    #     # mntihigh = item.find('mntihigh')
    #     # mntitop = item.find('mntitop')
    #     # print(mntiname.get_text(), mntiadd.get_text(),"\n", mntitop.get_text(), "\n", mntilistno.get_text())
################################################################################################################  
    # html2 = requests.get(url2, headers=headers).content
    res = requests.get(url2, headers=headers)
    html2 = res.content
    # time.sleep(5)
    soup2 = BeautifulSoup(html2, "lxml")
    word = soup2.find_all(id='wob_d')
    #vk_gy vk_sh
    #vk_gy vk_sh
    #vk_bk TylWce 전북 wob_tci

    weather_data = soup2.select_one('#wob_tci').__getitem__('alt')
    rain_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(1)').text.replace('강수확률: ', '', 1)
    Hum_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(2)').text.replace('습도: ', '', 1)
    wind_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(3)').text.replace('풍속: ', '', 1)
    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(1)
    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(2)
    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(3)
################################################################################################################  

    html1 = requests.get(url1, headers=headers).content
    # time.sleep(5)
    soup1 = BeautifulSoup(html1, "lxml")
    # img = soup1.find_all(class_='_img')
    img = soup1.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box')
    n = 1
    for x in range(1,4):
        #imgUrl = i['data-source']
        imgUrl = soup1.select_one(f'div:nth-child({x}) > a.thumb._thumb > img').__getitem__('data-source')
        img_data.append(imgUrl)
        #time.sleep(1)
        #print("-"*100)
        # with urlopen(imgUrl) as f:
        #     with open(f'./mountain/{class_}/' + class_ + str(n)+'.jpg','wb') as h: # w - write b - binary
        #         img = f.read()
        #         h.write(img)
        #         img_data.append(imgUrl)
        # n += 1
################################################################################################################  
    datas_mnt = data_mnt[i]
################################################################################################################  
    list_data.append([class_,address_,weather_data,rain_data,Hum_data,wind_data,img_data,datas_mnt])
################################################################################################################  
    today = date.today()
    now_timedata = today.year,'년', today.month,'월',today.day,'일', '월화수목금토일'[today.weekday()],'요일'
    today_timedata = str(now_timedata).replace(',','',10)
    today_timedata = today_timedata.replace("'","",10)
    print(today_timedata)
################################################################################################################  
    data = {'class_':class_, 'address_1':address_1, 'address_2':address_2, 'weather_data':weather_data, 'rain_data':rain_data, 'Hum_data':Hum_data, 'wind_data':wind_data, 'img_data':img_data, 'datas_mnt':datas_mnt, 'today_timedata':today_timedata}
    print('다운로드 완료',i)
    #print(list_data)

################################################################################################################
    with MongoClient(db_url) as client:
        mountaindb = client['mountain']
        infor = mountaindb.sampleCollection.insert_one(data)

################################################################################################################


