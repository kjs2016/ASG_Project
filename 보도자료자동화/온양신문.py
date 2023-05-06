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
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다
def ionyang(input):
    search_word = input
    input1=""
    input2="온양신문"
   
    start = time.time()
    # 브라우저 꺼짐 방지 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
    #driver = webdriver.Chrome(service = service, options=chrome_options)

    url = 'http://ionyang.com/default/search_list.php?board_data=c3RhcnRQYWdlJTNEMA==||&search_items=cGFydF9pZHglM0QlMjZtdWx0JTNEJTI2Z3JvdXBfaWQlM0QlMjZzX21vZGUlM0QlMjZyZXBvcnRlciUzRCUyNnN0YXJ0X2RheSUzRCUyNmVuZF9kYXklM0QlMjZzZWFyY2hfb3JkZXIlM0QlQkUlQzYlQkIlRUElQkQlQzMlQkQlQzMlQkMlQjMlQjAlRkMlQjglQUUlQjAlRjglQjQlREMlMjZhcmVhX3BhcnQlM0Q=||'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # p 태그 모두 찾기
    paragraphs = soup.find_all('p')

    # p 태그 하위의 a 태그의 텍스트 추출하여 리스트에 추가하기
    title_array = []
    for paragraph in paragraphs:
        links = paragraph.find_all('a')
        for link in links:
            title_array.append(link.text)

    title_array = list(filter(None, title_array))
    del title_array[20:len(title_array)]

    #titles = ul.select('a')

    #------titles변수는 리스트 이기 때문에 반복으로 출력해야 함-------#
    #for el in title_array:
        #print(el.text)
    # enumerate() 함수 사용
    #for i, item in enumerate(title_array):
       # print(i, item)
    #----------------------------------------------------------------#
    new_title_array=[]#기사 제목을 담을 배열 선언
    for title in title_array:
        new_title_array.append(title)

    #-------------------보도날짜 추출--------------------#
    date_array = []
    paragraphs = soup.find_all('font')
    for i in paragraph:
            date_array.append(i)

    #print(date_array)

    """
    date_array = soup.find_all("span","byline")
    new_date_array=[]#기사 날짜를 담을 배열 선언
    for date in date_array:
        new_date_array.append(date.text)

    for i in range(len(new_date_array)):
        new_date_array[i] = new_date_array[i][-15:-6]
        new_date_array[i] = new_date_array[i].replace(" ","")
        new_date_array[i] = new_date_array[i].replace(".", "")


    print(new_date_array) #날짜 데이터 배열 출력
    """
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
    print("cnt : ",cnt)
    print("num : ", num)
    #--------------------------------------------------#

    #print(link_text_array)#배열에 있는 내용 전부 출력
    link_date_array = [0] * 10

    if cnt > 0:
        driver = webdriver.Chrome(service = service, options=chrome_options)
        driver.get("http://ionyang.com/default/search_list.php?board_data=c3RhcnRQYWdlJTNEMA==||&search_items=cGFydF9pZHglM0QlMjZtdWx0JTNEJTI2Z3JvdXBfaWQlM0QlMjZzX21vZGUlM0QlMjZyZXBvcnRlciUzRCUyNnN0YXJ0X2RheSUzRCUyNmVuZF9kYXklM0QlMjZzZWFyY2hfb3JkZXIlM0QlQkUlQzYlQkIlRUElQkQlQzMlQkQlQzMlQkMlQjMlQjAlRkMlQjglQUUlQjAlRjglQjQlREMlMjZhcmVhX3BhcnQlM0Q=||")
        driver.implicitly_wait(5)
        if(num == 1):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/table[6]/tbody/tr/td[3]/table[7]/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/p/a').click()#첫번째 기사 클릭
        elif(num == 2):
            driver.find_element(By.XPATH, '/html/body/div[2]/div/table[6]/tbody/tr/td[3]/table[7]/tbody/tr[1]/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/p/a').click()#기사 2번째 클릭
        elif(num == 3):
            driver.find_element(By.XPATH, '/html/body/div[2]/div/table[6]/tbody/tr/td[3]/table[7]/tbody/tr[1]/td/table[3]/tbody/tr[2]/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/p/a').send_keys(Keys.ENTER)#기사 3번째 클릭
        elif(num == 4):
            driver.find_element(By.XPATH, '/html/body/div[2]/div/table[6]/tbody/tr/td[3]/table[7]/tbody/tr[1]/td/table[4]/tbody/tr[2]/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/p/a').send_keys(Keys.ENTER)#기사 4번째 클릭
        elif(num == 5):
            driver.find_element(By.XPATH, '/html/body/div[2]/div/table[6]/tbody/tr/td[3]/table[7]/tbody/tr[1]/td/table[5]/tbody/tr[2]/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/p/a').send_keys(Keys.ENTER)#기사 5번째 클릭
        else:
            print("그냥 진행합시다")

        time.sleep(1.5)
        """
        # p 태그 모두 찾기
        paragraphs = soup.find_all('td')

        date_array = []
        for paragraph in paragraphs:
            links = paragraph.find_all('p')
            for link in links:
                date_array.append(link.text)
        
        print(date_array)
        """

        
        #driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/table[6]/tbody/tr/td[3]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/p/a[4]').send_keys(Keys.ENTER)
        #time.sleep(5)
        print(driver.window_handles)
        #창 전환
        driver.switch_to.window(driver.window_handles[1])#새창으로 포커스 맞춤
        time.sleep(3)
        프린트모듈.Print_Control(input1, input2)
        time.sleep(8)
        driver.quit() 
        #print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간
    else:
        print("일치하는 내용이 없습니다")