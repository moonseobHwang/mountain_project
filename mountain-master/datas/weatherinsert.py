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


dataf = pd.read_csv('/home/rapa/Documents/mountain/file_name2.csv', encoding='utf-8')
mnt_data = pd.read_csv('/home/rapa/Documents/mountain/mountain1.csv', encoding='utf-8')
db_url='mongodb://127.0.0.1:27017'
headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
################################################################################################################  
input_data = []
dfc = []
dfn = []
df_data = []
k = 0
i = 0
df_s = []
df_so = []
dfsearch = []
class_label = []
################################################################################################################  
# with MongoClient(db_url) as client:
#     mountaindb = client['mountain']
# result1 = list(mountaindb.sampleCollection.find({}))
# df1 = pd.DataFrame(result1)

df1 = pd.DataFrame(dataf)
df1.set_index('class_', inplace=True)
count = 0

for k in range(0, 816):
    class_labels = df1['C_ad'][k]
    input_data.append(class_labels) # 자연데이터
    if df1.duplicated(['C_ad'])[k] != True: # 중복 제거
        dfc.append(class_labels) # 가공된 데이터기능
        dfsearch.append(class_labels) # 가공된 검색기능

# df1.index = input_data

#df.to_csv('yaksu.csv', encoding='utf-8')
# df1.loc['html_sendname']
try:
    MongoClient(db_url)['mountain'].weather.drop()
except:
    pass
################################################################################################################  
for i in range(0, 141):    
    try:
        soup2.clear()
    except:
        pass
################################################################################################################  
    #url2=f'https://www.google.com/search?q={dfc[i]}+기상정보'
    url2=f'https://search.naver.com/search.naver?&query={dfsearch[i]}+기상정보'
################################################################################################################  
    res = requests.get(url2, headers=headers)
    html2 = res.content
    soup2 = BeautifulSoup(html2, "lxml")
    print('겔겔겔')
    #vk_gy vk_sh
    #vk_gy vk_sh
    #vk_bk TylWce 전북 wob_tci
################################################################################################################  
    #온도
    #main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p > span.todaytemp
    #날씨설명
    #main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(1) > p
    #강수량
    #main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.table_info.weekly._weeklyWeather > ul:nth-child(2) > li:nth-child(1) > span.point_time.afternoon > span.rain_rate > span.num
    #오존
    #main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd.lv1 > span.num
    temp_data = soup2.select_one('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p > span.todaytemp').text
    weather_data = soup2.select_one('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(1) > p').text
    rain_data = soup2.select_one('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.table_info.weekly._weeklyWeather > ul:nth-child(2) > li:nth-child(1) > span.point_time.afternoon > span.rain_rate > span.num').text
    oz_data = soup2.select_one('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd:nth-child(6) > span.num').text
################################################################################################################  
#구글 정보 (실패 - 원인 - 창원시에서 누락 데이터 발생)
    # weather_data = soup2.select_one('#wob_tci').__getitem__('alt')
    # rain_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(1)').text.replace('강수확률: ', '', 1)
    # Hum_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(2)').text.replace('습도: ', '', 1)
    # wind_data = soup2.select_one('div > div.vk_gy.vk_sh > div:nth-child(3)').text.replace('풍속: ', '', 1)

    # list_data.append([dfc[i],weather_data,rain_data,Hum_data,wind_data])

    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(1)
    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(2)
    #wob_d > div > #div.vk_gy.vk_sh > div:nth-child(3)
################################################################################################################  
    print('다운로드 완료',i)
################################################################################################################  
    for j in range(0, 816):
        if input_data[j] == dfc[i]:
            df_s.append([dfc[i],temp_data,weather_data,rain_data,oz_data])
for z in range(0, 816):
    df_dt = {"class_":df1.index[z],"temp_data": df_s[z][1],"weather_data": df_s[z][2],"rain_data": df_s[z][3],"oz_data": df_s[z][4]}   
    df_so.append(df_dt)
################################################################################################################  
#data = {'class_':class_, 'C_ad':C_ad, 'weather_data':weather_data, 'rain_data':rain_data}
print('다운로드 완료',i)
#print(list_data)
################################################################################################################

df_datas = pd.DataFrame(df_so)
yaksu1 = pd.merge(df1, df_datas, left_on='class_', right_on='class_', how='left')   
yaksu2 = pd.merge(df1, df_datas, left_on='class_', right_on='class_', how='right')   
yaksu3 = pd.merge(df1, df_datas, on='class_', how='outer') 
df_datas.set_index('class_', inplace=True)
yaksu2 = dict(yaksu2)

# df_datas.to_csv('./df_datas.csv', sep=',', na_rep='NaN', encoding = 'utf-8')
# yaksu.to_csv('./file_name.csv', sep=',', na_rep='NaN', encoding = 'utf-8')
# yaksu1.to_csv('./file_name1.csv', sep=',', na_rep='NaN', encoding = 'utf-8')
# yaksu2.to_csv('./file_name2.csv', sep=',', na_rep='NaN', encoding = 'utf-8')
# yaksu3.to_csv('./file_name3.csv', sep=',', na_rep='NaN', encoding = 'utf-8')
################################################################################################################
with MongoClient(db_url) as client:
    mountaindb = client['mountain']
################################################################################################################
for l in range(0, 816):
    data = {

        "class_":yaksu2['class_'][l],
        "Address_1":f"{yaksu2['Address_1'][l]}",
        "Address_2":f"{yaksu2['Address_2'][l]}",
        "use_p":f"{yaksu2['use_p'][l]}",
        "research_date":yaksu2['research_date'][l],
        "research":yaksu2['research'][l],
        "phone_num":yaksu2['phone_num'][l],
        "C_ad1":yaksu2['C_ad1'][l],
        "C_ad":yaksu2['C_ad'][l],
        "temp_data_y":yaksu2['temp_data_y'][l],
        "weather_data_y":yaksu2['weather_data_y'][l],
        "rain_data_y":yaksu2['rain_data_y'][l],
        "oz_data_y":yaksu2['oz_data_y'][l],
        }   
    
    infor = mountaindb.yaksu.insert_one(data)