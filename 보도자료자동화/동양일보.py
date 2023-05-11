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


def dynews15(input):
    kisatitle = "동양일보"
    date_v = ""

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치

    url = 'http://prt.dynews.co.kr/engine_yonhap/search.php?div_code=&cust_div_code=&sfield=&article_type=&others_cont_type=&period=all&from_date=&to_date=&searchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&picktab=article&sort=date'
    
    search_word = input
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #search_results = soup.find_all('div', class_='newsList01')
    #search_results = soup.find_all("div", "articleArea")
    search_results = soup.find_all('strong')

    print(search_results)

    new_title_array=[]#기사 제목을 담을 배열 선언

        #----------------------------------------------------------------#
    new_title_array=[]#기사 제목을 담을 배열 선언
    for title in search_results:
        new_title_array.append(title.text)
    # 선택된 모든 div 태그에 대해 a 태그 검색
    #for result in search_results:
        #a_tags = result.find_all("b")
        #for tag in a_tags:
            #new_title_array.append(tag.text)
    #search_results = soup.find_all('div', class_='newsList01')
    #title_array = soup.find_all("strong","title")
        #titles = ul.select('a')

        #------titles변수는 리스트 이기 때문에 반복으로 출력해야 함-------#
        #for el in title_array:
            #print(el.text)
        # enumerate() 함수 사용
    for i, item in enumerate(new_title_array):
        print(i, item)
        #----------------------------------------------------------------#
    #new_title_array=[]#기사 제목을 담을 배열 선언
    #for title in title_array:
        #new_title_array.append(title.text)
    # 선택된 모든 div 태그에 대해 a 태그 검색
    #for result in search_results:
        #a_tags = result.find_all("a")
        #for tag in a_tags:
            #new_title_array.append(tag.text)

            
    #print("---------------")
    #print("0번째"+new_title_array[0])
    #print("1번째"+new_title_array[1])
    #print("2번째"+new_title_array[2])
    #print("3번째"+new_title_array[3])
    #print("---------------")

    #---------새창보기 배열 제거------#
    #value = '[새창보기]'
    #new_title_array = list(filter(lambda x: x != value, new_title_array))

    #print(new_title_array)

    #배열 요소와 값 함께 출력
    #for i, item in enumerate(new_title_array):
            #print(i, item)


    """
    #-------------------보도날짜 추출--------------------#
    date_array = soup.find_all("dd","etc")
    new_date_array=[]#보도 날짜를 담을 배열 선언
    for date in date_array:
        new_date_array.append(date)
    print(new_date_array)

    for i in range(len(new_date_array)):
        new_date_array[i] = new_date_array[i][-15:-6]
        new_date_array[i] = new_date_array[i].replace(" ","")
        new_date_array[i] = new_date_array[i].replace(".", "")
    """
    #print(new_date_array) #날짜 데이터 배열 출력
    #print(len(new_date_array)) 날짜 들어있는 배열 출력
    #----------------------------------------------------#

    #--------제목에서 일치하는 단어가 있는 탐색---------#
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
            #break
        else:
            continue
    print("cnt : ",cnt)
    print("num : ", num)
    #--------------------------------------------------#
    time.sleep(1)

    #--------제목이 일치한다면 스크랩 수행--------------#
    if cnt > 0:
        driver = webdriver.Chrome(service = service, options=chrome_options)
        #driver.get("https://prt.cctoday.co.kr/engine_yonhap/search.php?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&_ga=2.211558610.658557104.1682583195-73037611.1681804658")
        driver.get("http://prt.dynews.co.kr/engine_yonhap/search.php?div_code=&cust_div_code=&sfield=&article_type=&others_cont_type=&period=all&from_date=&to_date=&searchword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&picktab=article&sort=date")
        driver.implicitly_wait(5)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        if(num == 7):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div/div[2]/div[1]/div[2]/div/a').send_keys(Keys.ENTER)#기사 1번째 클릭
        elif(num == 8):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div/div[2]/div[2]/div/div/a').send_keys(Keys.ENTER)#기사 2번째 클릭
        elif(num == 9):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div/div[2]/div[3]/div[2]/div/a').send_keys(Keys.ENTER)
        elif(num == 10):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div/div[2]/div[4]/div[2]/div/a').send_keys(Keys.ENTER)
        elif(num == 5):
            driver.find_element(By.XPATH, '//*[@id="ulListType"]/li[5]/a').send_keys(Keys.ENTER)
        elif(num == 6):
            driver.find_element(By.XPATH, '//*[@id="ulListType"]/li[6]/a').send_keys(Keys.ENTER)
        elif(num == 7):
            driver.find_element(By.XPATH, '//*[@id="ulListType"]/li[7]/a').send_keys(Keys.ENTER)
        else:
            print("더 이상 비교할 수 없습니다")

        driver.implicitly_wait(5)
        #----------------보도 날짜 추출--------------------#
        date_array = soup.find_all('span','btw')
        new_date_array=[]#기사 날짜를 담을 배열 선언
        for date in date_array:
            new_date_array.append(date)

        print(new_date_array)
        #date_array = soup.find_all("span","btw")
        #new_date_array=[]#보도 날짜를 담을 배열 선언
        #for date in date_array:
            #new_date_array.append(date.text)
            #print(new_date_array)
        
        # for i in range(len(new_date_array)):
            #new_date_array[i] = new_date_array[i][-17:-9]
            #new_date_array[i] = new_date_array[i].replace("/","")
            ##new_date_array[i] = new_date_array[i].replace(".", "")

        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH,'//*[@id="article-view"]/div/header/div/article[2]/div/button[1]').send_keys(Keys.ENTER)
        #try:
        #element = driver.find_element(By.CSS_SELECTOR, '.tool')
    # except NoSuchElementException:
        # print("Element not found")
        #time.sleep(5)
        #pag.moveTo(1429, 504, 0.5)
        #pag.click()
        time.sleep(1)
        #print(driver.window_handles)
        #창 전환
        #driver.switch_to.window(driver.window_handles[1])
        
        #time.sleep(3)
        #driver.switch_to.window(driver.window_handles[1])#새창으로 포커스 맞춤
        프린트모듈.Print_Control(date_v, kisatitle)
        time.sleep(8)
        driver.quit()
    else:
         print("일치하는 내용이 없습니다")

    time.sleep(6)