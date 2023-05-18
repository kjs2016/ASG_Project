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


def jbnews41(input):
    kisatitle = "중부매일"
    date_v = ""


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치

    #코드 실행시간 start저장
    search_word = input
    start = time.time()

    url = 'http://prt.jbnews.com/engine_yonhap/search.php?picktab=all&searchcont=yonhap&div_code=&others_cont_type=&orgsearchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&page=1&sort=&from_date=&to_date=&searchword2=&cust_div_code=&searchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #search_results = soup.find_all('div', class_='newsList01')
    search_results = soup.find_all("div","title")

    print(search_results)

    new_title_array=[]#기사 제목을 담을 배열 선언

    # 선택된 모든 div 태그에 대해 a 태그 검색
    for result in search_results:
        a_tags = result.find_all("a")
        for tag in a_tags:
            new_title_array.append(tag.text)
    #-------------------보도날짜 추출--------------------#
    date_array = soup.find_all("span","byline")
    new_date_array=[]#기사 날짜를 담을 배열 선언
    for date in date_array:
        new_date_array.append(date.text)

    for i in range(len(new_date_array)):
        new_date_array[i] = new_date_array[i][-15:-6]
        new_date_array[i] = new_date_array[i].replace(" ","")
        new_date_array[i] = new_date_array[i].replace(".", "")


    #print(new_date_array) #날짜 데이터 배열 출력
    #print(len(new_date_array)) 날짜 들어있는 배열 출력
    #----------------------------------------------------#

    #--------제목에서 일치하는 단어가 있는 탐색---------#
    cnt = 0
    num = 0#배열의 요소 세는 변수
    for i in range(len(new_title_array)):#배열에 길이만큼 반복
        a = new_title_array[i].find(search_word)#배열에 0번째 요소에 있는 문자열중에 search_word변수에 담겨있는 단어가 들어있는지 확인(들어있다 = 양수, 없다 = 음수)
        new_title_array[i] = new_title_array[i].replace(" ","")#배열에 들어있는 제목 띄어쓰기 전부 제거
        b = new_title_array[i].find(search_word)#다시 단어 찾기
        num = num + 1
        print(new_title_array[i])  
        if a > -1 or b > -1:#들어있으면 cnt 카운트 
            cnt = cnt + 1
            break
        else:
            continue
    #print("cnt : ",cnt)
    #print("num : ", num)
    #--------------------------------------------------#

    #print(link_text_array)#배열에 있는 내용 전부 출력
    link_date_array = [0] * 10

    if cnt > 0:
        driver = webdriver.Chrome(service = service, options=chrome_options)
        #driver.get("https://prt.cctoday.co.kr/engine_yonhap/search.php?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&_ga=2.211558610.658557104.1682583195-73037611.1681804658")
        driver.get("http://prt.jbnews.com/engine_yonhap/search.php?picktab=all&searchcont=yonhap&div_code=&others_cont_type=&orgsearchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&page=1&sort=&from_date=&to_date=&searchword2=&cust_div_code=&searchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8")
        driver.implicitly_wait(5)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        if(num == 1):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').send_keys(Keys.ENTER)#기사 1번째 클릭
        elif(num == 2):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[1]/div[2]/div[2]/div[2]/div/a').send_keys(Keys.ENTER)#기사 2번째 클릭
        elif(num == 3):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[1]/div[2]/div[3]/div[2]/div/a').send_keys(Keys.ENTER)
        elif(num == 4):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[1]/div[2]/div[4]/div[2]/div/a').send_keys(Keys.ENTER)
        elif(num == 5):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[1]/div[2]/div[5]/div[2]/div/a').send_keys(Keys.ENTER)
        else:
            print("그냥 진행합시다")

        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH,'//*[@id="article-view"]/div/header/div/article[2]/div/button[1]').send_keys(Keys.ENTER)
        #time.sleep(5)
        #창 전환
        #driver.switch_to.window(driver.window_handles[1])#새창으로 포커스 맞춤
        프린트모듈.Print_Control(date_v, kisatitle)
        time.sleep(4)
        driver.quit() 
        #print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간
    else:
        print("일치하는 내용이 없습니다")

    time.sleep(6)