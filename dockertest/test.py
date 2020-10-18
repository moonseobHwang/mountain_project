import bs4, time, selenium, requests, json, schedule
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymongo import MongoClient

driver = webdriver.Chrome('C:\\Users\\USER\\Desktop\\dockertest\\chromedriver')
db_url='mongodb://127.0.0.1:27017'
# driver.get('https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=133100%2C133101%2C133200%2C134101%2C134102&rot2WorkYn=&templateInfo=&payGbn=&resultCnt=10&keywordJobCont=&cert=&cloDateStdt=&moreCon=more&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&keywordStaAreaNm=&maxPay=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=1&region=&resultCntInfo=10&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=N&searchOn=Y&subEmpHopeYn=&academicGbn=04&foriegn=&templateDepthNoInfo=&mealOfferClcd=&station=&moerButtonYn=&holidayGbn=&enterPriseGbn=all&academicGbnoEdu=&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=5c5ab007-f9f9-4c7c-88fe-f811bf6c31f3&keywordBusiNm=&preferentialGbn=all&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex={}&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL')
# MongoClient(db_url)['work'].sampleCollection.drop()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://bac.blackyak.com/html/challenge/ChallengeVisitList.asp?CaProgram_key=114')

# 이름
# //*[@id="VisitRecordList"]/ul/li[1]/div/div[2]/span[1]
# //*[@id="VisitRecordList"]/ul/li[2]/div/div[2]/span[1]

# 좌표
# //*[@id="VisitRecordList"]/ul/li[1]/div/div[2]/a

for i in range(1, 101):
    C_name = driver.find_element_by_xpath(f'//*[@id="VisitRecordList"]/ul/li[{i}]/div/div[2]/span[1]').text
    C_gps = driver.find_element_by_xpath(f'//*[@id="VisitRecordList"]/ul/li[{i}]/div/div[2]/a').text

    data = {'C_gps': C_gps, 'C_name':C_name}
    print(data)
