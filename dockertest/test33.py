from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests, time, bs4, sqlite3, schedule, selenium, json, urllib, urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

mountain_data = pd.read_csv('C:/Users/USER/Desktop/dockertest/mountain1.csv', encoding='utf-8')
# weather_data = pd.read_csv('C:/Users/USER/Desktop/dockertest/.csv', encoding='utf-8')
# Gps_data = pd.read_csv('C:/Users/USER/Desktop/dockertest/지점상세정보.csv', encoding='utf-8')
# name=str(input("산이름을 입력하세요 :"))


for i in range(1, 101):
    mountain_datas = pd.DataFrame(mountain_data, index=[i])
    class_ = str(mountain_datas['이름']).replace('\nName: 이름', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    address_ = str(mountain_datas['높이']).replace('\nName: 높이', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    address_1 = str(mountain_datas['소재지']).replace('\nName: 소재지', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    data={'class_':class_, 'address_':address_, 'address_1':address_1}

    for names in range(1, 2):
        url = f'http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI?serviceKey=cRhBhi3sxVClCIks%2FemvBBGZgcYv5HaKvFr26Ov5Q5nor0WtrgUNO9rwfYO6FkLUif9SefP0BK%2B18mBFvV8%2FCw%3D%3D&searchWrd={class_}'
        response = requests.get(url)
        # print(response.status_code)
        # print(response.text)


        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find_all('item')

        for item in data:
            mntiname = item.find('mntiname')
            mntiadd = item.find('mntiadd')
            mntidetails = item.find('mntidetails')
            mntitop = item.find('mntitop')
            mntilistno = item.find('mntilistno')
            # mntitop = item.find('mntitop')
            # mntitop = item.find('mntitop')
            print(mntiname.get_text(), mntiadd.get_text(),"\n", mntitop.get_text(), "\n", mntilistno.get_text())

# db_url='mongodb://172.17.0.2:27017'
# with MongoClient(db_url) as client:
# mountindb = client['mountin']


# url = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/detailImage'
# queryParams = '북한산' + urlencode({ quote_plus('ServiceKey') : '0c%2BeEdG%2Fbkm34OVKN%2BIMu9QP0kI1eNbPqitvIGQz15VBbq1nM8BJEcdPZqWZGSsqNLzEWe0R4qJnHqmmDEQHjA%3D%3D', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('MobileOS') : 'ETC', quote_plus('MobileApp') : 'AppTest', quote_plus('contentId') : '1392583', quote_plus('imageYN') : 'Y', quote_plus('subImageYN') : 'Y' })

# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print(response_body)
