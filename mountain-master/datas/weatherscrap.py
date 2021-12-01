import bs4, time, selenium, requests, json, schedule, csv, os, urllib, urllib3, datetime
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
from datetime import date

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
    MongoClient(db_url)['mountain'].weather.drop()
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
        soup2.clear()
    except:
        pass
    mountain_datas = pd.DataFrame(mountain_data, index=[i])
    class_ = str(mountain_datas['C_name']).replace('\nName: C_name', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    address_ = str(mountain_datas['C_gps']).replace('\nName: C_gps', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    C_ad = str(mountain_datas['C_ad']).replace('\nName: C_ad', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    # try:
    #     if class_[-1]= ')':
    # except:
        # pass
    url2 = f'https://www.google.com/search?q={C_ad} 기상정보'
################################################################################################################  
    # html2 = requests.get(url2, headers=headers).content
    res = requests.get(url2, headers=headers)
    html2 = res.content
    time.sleep(5)
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
    today = date.today()
    now_timedata = today.year,'년', today.month,'월',today.day,'일', '월화수목금토일'[today.weekday()],'요일'
    today_timedata = str(now_timedata).replace(',','',10)
    today_timedata = today_timedata.replace("'","",10)
    print(today_timedata)
################################################################################################################  
    list_data.append([class_,C_ad,weather_data,rain_data,Hum_data,wind_data,today_timedata])
################################################################################################################  
    data = {'class_':class_, 'C_ad':C_ad, 'weather_data':weather_data, 'rain_data':rain_data, 'Hum_data':Hum_data, 'wind_data':wind_data, 'today_timedata':today_timedata}
    print('다운로드 완료',i)
    #print(list_data)
################################################################################################################
    with MongoClient(db_url) as client:
        mountaindb = client['mountain']
    infor = mountaindb.weather.insert_one(data)
################################################################################################################


