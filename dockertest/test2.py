from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests, time, bs4, sqlite3, schedule

url = "http://bac.blackyak.com/html/challenge/ChallengeVisitList.asp?CaProgram_key=114"
header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

# 이름
#VisitRecordList > ul > li:nth-child(1) > div > div.text > span:nth-child(1)
#VisitRecordList > ul > li:nth-child(2) > div > div.text > span:nth-child(1)

# 좌표
#VisitRecordList > ul > li:nth-child(1) > div > div.text > a
#VisitRecordList > ul > li:nth-child(2) > div > div.text > a

res = requests.get(url)
soup = BeautifulSoup(res.text, "html5lib")
title_data=soup.section

for i in range(1, 101):
    datas = title_data.select(f"div.VisitRecordList > ul > li:nth-of-type({i})")

    for data in datas: # i를 key가앖으로 받아주고 그가앖을 토대로 데이터를 선별해준다
        try:
            #이름
            name_data = data.select_one("div > div.text > span:nth-of-type(1)")
            name_data = str.strip(name_data.get_text())
            #좌표
            GPS_data = data.select_one("div > div.text > a")
            GPS_data = str.strip(GPS_data.get_text())

            data={'GPS_data':GPS_data, 'name_data':name_data}
            print(data)
        except:
            pass

    time.sleep(0.5)