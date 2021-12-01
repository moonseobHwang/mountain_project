import bs4, requests, json, schedule, csv, os, urllib, urllib3
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import numpy as np
from urllib.parse import quote_plus
from urllib.request import urlopen
from datetime import date, time, datetime

mountain_data = pd.read_csv('/home/rapa/Documents/mountain/mtngps.csv', encoding='utf-8')
db_url='mongodb://127.0.0.1:27017'


for i in range(0, 100):
    mountain_datas = pd.DataFrame(mountain_data, index=[i])
    class_ = str(mountain_datas['C_name']).replace('\nName: C_name', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)
    C_ad = str(mountain_datas['C_ad']).replace('\nName: C_ad', '', 1).replace(f'{i}    ', '', 1).replace(', dtype: object','', 1)

    with MongoClient(db_url) as client:
        mountaindb = client['mountain']
        cursor = mountaindb.sampleCollection.find({"class_":class_})
        for student in cursor :
            mountaindb.sampleCollection.update_one(student,{'$set': {'C_ad':C_ad}})

