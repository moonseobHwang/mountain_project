from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import requests, csv

# 실행 안해도 됨, 바로 mountainscrap.py를 실행하기!
driver = webdriver.Chrome(executable_path='/home/rapa/Documents/mountain/chromedriver')
db_url='mongodb://127.0.0.1:27017'
driver.get('http://bac.blackyak.com/html/challenge/ChallengeVisitList.asp?CaProgram_key=114')

f = open('mtngps.csv', 'wt', encoding='utf-8') # csv file 생성
data = {'C_name', 'C_gps1', 'C_gps2'} # colum설정
writer = csv.DictWriter(f,fieldnames=data)
writer.writeheader()

for i in range(1, 101):
    C_name = driver.find_element_by_xpath(f'//*[@id="VisitRecordList"]/ul/li[{i}]/div/div[2]/span[1]').text
    C_gps = driver.find_element_by_xpath(f'//*[@id="VisitRecordList"]/ul/li[{i}]/div/div[2]/a').text
    C_gps = C_gps.split(',')
    C_gps1 = C_gps[0]
    C_gps2 = C_gps[1]
    data = {'C_name':C_name, 'C_gps1':C_gps1, 'C_gps2':C_gps2}
    writer.writerow({'C_name':C_name,'C_gps1': C_gps1, 'C_gps2':C_gps2})
    print(data)

f.close()