import pandas as pd
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 전체 클릭하기
chrome = webdriver.Chrome()
#kia 홈페이지 들어가기
chrome.get('https://www.kia.com/kr/customer-service/center/faq')
chrome.implicitly_wait(30)
html = chrome.page_source
notices = chrome.find_elements(By.CLASS_NAME, value="tabs__btn")
notices[1].click()    #전체 카테고리 클릭하기

#질문 추출 함수
def f_question(num : int):
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select(".cmp-accordion__title")

    
    for n in notices:
        r = n.get_text()
        pages_question.append(r)

#응답 추출 함수
def f_answer(num : int):
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notice = soup.select(".faqinner__wrap > div")

    for n in notice:
        print(n.get_text())
        r = n.get_text()
        pages_answer.append(r)

pages_question=[]
pages_answer=[]

for j in range(1,5):
    for i in range(1,6):
        notice = chrome.find_elements(By.CSS_SELECTOR, f"#contents > div > div.container.responsivegrid.aem-GridColumn.aem-GridColumn--default--12 > div > div > div.faq-bottom-paging.spacing-pt3.spacing-pb3 > div > ul > li:nth-child({i}) > a")
        notice[0].click()

        f_question(i)
        f_answer(i)
    
    btn = chrome.find_elements(By.CLASS_NAME, "pagigation-btn-next")
    btn[0].click()

kia={'질문':pages_question,
'답변':pages_answer,
'식별자':['기아']*200}
kia_frame = pd.DataFrame(kia)
con = pymysql.connect(host='localhost', user='root', password='root1234', db='car_registration_status', charset='utf8', autocommit=False) 
cur = con.cursor(pymysql.cursors.DictCursor)

question = kia_frame['질문']
answer = kia_frame['답변']
vender = kia_frame['식별자']

for i in range(200):
    answer[i] = answer[i].replace('\'','')
    question[i] = question[i].replace('\'','')
    answer[i] =answer[i].replace('\"','')
    question[i] = question[i].replace('\"','')
    sql = "INSERT INTO QandA (question,answer,vender) VALUES (\"%s\", \"%s\", \"%s\");" % (question[i],answer[i],vender[i])
    cur.execute(sql)
    cur.execute("commit;")