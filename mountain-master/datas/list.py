from selenium import webdriver as dr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
import requests, time

driver = dr.Chrome(executable_path='/home/rapa/Documents/mountain/chromedriver') # Chromedriver 경로 확인
for pg in range(1,11): # paging 1pg to 10 pg
    driver.get(url=f'http://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex={pg}&searchMnt=&searchCnd=10&mn=NKFS_03_01_12&orgId=&mntUnit=10') # 산림청 홈페이지

    for num in range(1,11): # list 1 to 10
        name = driver.find_element_by_xpath(f'//*[@id="txt"]/ul/li[{num}]/a/div/div[2]/strong').text # name
        height = driver.find_element_by_xpath(f'//*[@id="txt"]/ul/li[{num}]/a/div/div[2]/ul/li[1]/span[2]').text # height 
        address = driver.find_element_by_xpath(f'//*[@id="txt"]/ul/li[{num}]/a/div/div[2]/ul/li[2]/span[2]').text # address
        
        t_xpath = '//*[@id="txt"]/ul/li[{}]/a/div'.format(pg) # 클릭할 곳
        driver.find_element_by_xpath(t_xpath).click() # 클릭으로 오픈
        time.sleep(5) # 윈도우 창이 열릴 때 까지 기다려야 됨
        contents = driver.find_element_by_xpath('//*[@id="txt"]/p[1]').text # 특징 및 선정이유
        contents = contents.replace('\n','',1000)

        with MongoClient('mongodb://127.0.0.1:27017') as client:
            mtlist = client['mtlist']
            colums = {'이름':name, '높이':height, '소재지':address, '내용':contents}
            mtlist.mountain.insert_one(colums)

        driver.back()