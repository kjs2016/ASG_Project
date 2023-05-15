from selenium.webdriver.chrome.options import Options
from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, 프린트모듈
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 업데이트
from selenium.webdriver.chrome.service import Service
import pyautogui as pag
import pyperclip
import os
from pprint import pprint as pp
import requests
from lxml import html
from selenium.common.exceptions import NoSuchElementException
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.

def daejonilbo21(input):
    kisatitle = "대전일보"
    date_v = ""

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치

    #코드 실행시간 start저장
    search_word = input
    start = time.time()

    
    url = "http://www.daejonilbo.com/news/articleList.html"

    headers = {
        "Referer" : "http://www.daejonilbo.com",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    data = {
        "sc_area": "A",
        "view_type": "sm",
        "sc_word": "아산시시설관리공단"   
    }
        

    res = requests.post(url, headers = headers, data=data)
    print(res.text)

    soup = BeautifulSoup(res.text, "lxml")
    search_results = soup.find_all("h4", class_="titles line-6x3")

    new_title_array=[]#기사 제목을 담을 배열 선언

        # 선택된 모든 div 태그에 대해 a 태그 검색
    for result in search_results:
        a_tags = result.find_all("a")
        for tag in a_tags:
            new_title_array.append(tag.text)

    #배열 요소와 값 함께 출력
    for i, item in enumerate(new_title_array):
        print(i, item)

    cnt = 0
    num = 0#배열의 요소 세는 변수
    t = 1
    for i in range(len(new_title_array)):#배열에 길이만큼 반복
        a = new_title_array[i].find(search_word)#배열에 0번째 요소에 있는 문자열중에 search_word변수에 담겨있는 단어가 들어있는지 확인(들어있다 = 양수, 없다 = 음수)
        new_title_array[i] = new_title_array[i].replace(" ","")#배열에 들어있는 제목 띄어쓰기 전부 제거
        b = new_title_array[i].find(search_word)#다시 단어 찾기
        num = num + 1
        print(new_title_array[i])
        #t = t + 4  
        if a > -1 or b > -1:#들어있으면 cnt 카운트 
            cnt = cnt + 1
            break
        #elif t > 118:
        # break
        else:
            continue
    print("cnt : ",cnt)
    print("num : ", num)
    link_date_array = [0] * 10

    if cnt > 0:
        service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        query_txt = '아산시시설관리공단'
        a = 'sc_word'
        driver = webdriver.Chrome(service = service, options=chrome_options)
        driver.get("http://www.daejonilbo.com/")
        time.sleep(1)

        element = driver.find_element(By.NAME, a)#검색창 html의 name이 'q'여서 q다
        element.send_keys(query_txt)               #검색 단어를 입력한다
        element.submit()
        time.sleep(1)
        driver.implicitly_wait(5)
        if(num == 1):
            driver.find_element(By.XPATH,'//*[@id="section-list"]/ul/li[1]/div/h4/a').click()#첫번째 기사 클릭
        elif(num == 2):
             driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[2]/h4/a').click()#기사 2번째 클릭
        elif(num == 3):
             driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[3]/h4/a').send_keys(Keys.ENTER)#기사 3번째 클릭
        elif(num == 4):
            driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[4]/h4/a').send_keys(Keys.ENTER)#기사 4번째 클릭
        elif(num == 5):
            driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[5]/h4/a').send_keys(Keys.ENTER)#기사 5번째 클릭
        else:
            print("그냥 진행합시다")
        #driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//*[@id="articleViewCon"]/article/header/div[2]/article/section[2]/button[1]').send_keys(Keys.ENTER)
        #time.sleep(5)
        print(driver.window_handles)
        #창 전환
        driver.switch_to.window(driver.window_handles[1])#새창으로 포커스 맞춤
        프린트모듈.Print_Control(date_v, kisatitle)
        time.sleep(8)
        driver.quit() 
        #print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간
    else:
        print("일치하는 내용이 없습니다")

    time.sleep(6)