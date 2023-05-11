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
import time
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 업데이트
from selenium.webdriver.chrome.service import Service
import pyautogui as pag
import pyperclip
import os
from pprint import pprint as pp
import requests
import 프린트모듈
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.
def ccsimin18(input):
    
    kisatitle = "충남신문" 
    date_v = ""

    search_word = input

    start = time.time()

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치

    url = 'http://www.ccsimin.com/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&imageField.x=0&imageField.y=0'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    search_results = soup.find_all("div", class_="search_result_list_box")

    new_title_array=[]#기사 제목을 담을 배열 선언

    # 선택된 모든 div 태그에 대해 a 태그 검색
    for result in search_results:
        a_tags = result.find_all("a")
        for tag in a_tags:
            new_title_array.append(tag.text)
            

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
        a = new_title_array[t].find(search_word)#배열에 0번째 요소에 있는 문자열중에 search_word변수에 담겨있는 단어가 들어있는지 확인(들어있다 = 양수, 없다 = 음수)
        new_title_array[t] = new_title_array[t].replace(" ","")#배열에 들어있는 제목 띄어쓰기 전부 제거
        b = new_title_array[t].find(search_word)#다시 단어 찾기
        num = num + 1
        print(new_title_array[i])
        t = t + 4  
        if a > -1 or b > -1:#들어있으면 cnt 카운트 
            cnt = cnt + 1
            break
        elif t > 118:
            break
        else:
            continue
    print("cnt : ",cnt)
    print("num : ", num)
    #--------------------------------------------------#

    #--------제목이 일치한다면 스크랩 수행--------------#
    if cnt > 0:
        driver = webdriver.Chrome(service = service, options=chrome_options)
        #driver.get("https://prt.cctoday.co.kr/engine_yonhap/search.php?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&_ga=2.211558610.658557104.1682583195-73037611.1681804658")
        driver.get("http://www.ccsimin.com/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&imageField.x=0&imageField.y=0")
        driver.implicitly_wait(5)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        if(num == 1):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[1]/dl/dt/a').click()#기사 1번째 클릭
        elif(num == 2):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[2]/dl/dt/a').click()#기사 2번째 클릭
        elif(num == 3):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[3]/dl/dt/a').click()#기사 3번째 클릭
        elif(num == 4):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[4]/dl/dt/a').click()#기사 4번째 클릭
        elif(num == 5):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[5]/dl/dt/a').click()#기사 5번째 클릭
        elif(num == 6):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[6]/dl/dt/a').click()#기사 6번째 클릭
        elif(num == 7):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[7]/dl/dt/a').click()#기사 7번째 클릭
        elif(num == 8):
            driver.find_element(By.XPATH, '//*[@id="search_result"]/div[2]/div[8]/dl/dt/a').click()#기사 8번째 클릭
        else:
            print("더 이상 비교할 수 없습니다")
        """
        driver.implicitly_wait(5)
        #----------------보도 날짜 추출--------------------#
        btw_span = soup.find("span", {"class": "edit_time"}).text
        btw_span = btw_span.replace(".", "")
        btw_span = btw_span[-14:-8]
        """
        #print(btw_span)
        #date_array = soup.find_all("span","btw")
        #new_date_array=[]#보도 날짜를 담을 배열 선언
        #for date in date_array:
            #new_date_array.append(date.text)
            #print(new_date_array)
        
       # for i in range(len(new_date_array)):
            #new_date_array[i] = new_date_array[i][-17:-9]
            #new_date_array[i] = new_date_array[i].replace("/","")
            ##new_date_array[i] = new_date_array[i].replace(".", "")

        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="wrap"]/div[3]/div[2]/div[3]/ul/li[2]/a').send_keys(Keys.ENTER)
        #time.sleep(5)
       #print(driver.window_handles)
        #창 전환
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        프린트모듈.Print_Control(date_v,kisatitle)
        time.sleep(10) 
        #pag.moveTo(214, 899)#파일명 쓰는 칸으로 이동
        #pag.click()
        #pag.dragRel(-30, 0, 2, button='left')#윈쪽으로 드래그
        driver.quit() 
  #제목이 일치하지 않으면 스크랩 수행 안함
    else:
        print("제목과 일치하지 않습니다")        
    
    #print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간
