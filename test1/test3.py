from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests, time, bs4, sqlite3, schedule, selenium, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
db_url='mongodb://172.17.0.2:27017'



with MongoClient(db_url) as client:
    mountindb = client['mountin']
    yaksu_data = pd.read_csv('/home/aa6271235/Downloads/yaksu/yaksu.csv', encoding='euc-kr')

    for i in range(0, 1490):
        yaksu_datas = pd.DataFrame(yaksu_data, index=[i])
        class_ = str(yaksu_datas['약수터명']).replace('\nName: 약수터명', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        address_ = str(yaksu_datas['데이터기준일자']).replace('\nName: 데이터기준일자', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        address_1 = str(yaksu_datas['소재지지번주소']).replace('\nName: 소재지지번주소', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        address_2_0 = str(yaksu_datas['위도']).replace('\nName: 위도', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: float64','', 1)
        address_2_1 = str(yaksu_datas['경도']).replace('\nName: 경도', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: float64','', 1)
        address_3 = str(yaksu_datas['수질검사결과구분']).replace('\nName: 수질검사결과구분', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        address_4 = str(yaksu_datas['관리기관명']).replace('\nName: 관리기관명', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        address_5 = str(yaksu_datas['관리기관전화번호']).replace('\nName: 관리기관전화번호', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
        data={'class_':class_, 'address_':address_, 'address_1':address_1, 'address_2_0':address_2_0, 'address_2_1':address_2_1, 'address_3':address_3, 'address_4':address_4, 'address_5':address_5}
        #infor = mountindb.sampleCollection.insert_one(data)