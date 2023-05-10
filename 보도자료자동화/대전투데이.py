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

def daejeontoday12(input):
    kisatitle = "대전투데이"
    date_v = ""

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치

    #코드 실행시간 start저장
    search_word = input
    start = time.time()

    url = 'http://www.daejeontoday.com/news/articleList.html?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # find_all 메소드를 사용하여 태그가 nobr이고 class가 titles인 요소들을 모두 가져옵니다.
    #ul = soup.select_one('h4.titles')
    title_array = soup.find_all("h4","titles")
    #titles = ul.select('a')

    #------titles변수는 리스트 이기 때문에 반복으로 출력해야 함-------#
    #for el in title_array:
        #print(el.text)
    # enumerate() 함수 사용
    for i, item in enumerate(title_array):
        print(i, item.text)
    #----------------------------------------------------------------#
    new_title_array=[]#기사 제목을 담을 배열 선언
    for title in title_array:
        new_title_array.append(title.text)

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
        driver.get("http://www.daejeontoday.com/news/articleList.html?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8")
        driver.implicitly_wait(5)
        if(num == 1):
            driver.find_element(By.XPATH,'//*[@id="section-list"]/ul/li[1]/h4/a').click()#첫번째 기사 클릭
            date_v = new_date_array[0]
        elif(num == 2):
             driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[2]/h4/a').click()#기사 2번째 클릭
             date_v = new_date_array[1]
        elif(num == 3):
             driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[3]/h4/a').send_keys(Keys.ENTER)#기사 3번째 클릭
             date_v = new_date_array[2]
        elif(num == 4):
            driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[4]/h4/a').send_keys(Keys.ENTER)#기사 4번째 클릭
            date_v = new_date_array[3]
        elif(num == 5):
            driver.find_element(By.XPATH, '//*[@id="section-list"]/ul/li[5]/h4/a').send_keys(Keys.ENTER)#기사 5번째 클릭
            date_v = new_date_array[4]
        else:
            print("그냥 진행합시다")
        #driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//*[@id="article-view"]/div/header/div/article[2]/div/button[1]').send_keys(Keys.ENTER)
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