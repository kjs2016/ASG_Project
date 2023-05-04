from selenium.webdriver.chrome.options import Options
from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 업데이트
from selenium.webdriver.chrome.service import Service
import pyautogui as pag
import pyperclip
import os
import shutil
#import PrintViewControl as pvc
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.

def print_click():
    pag.moveTo(1228, 841)
    pag.click()  

start = time.time()
path = 'C:/Users/User/Desktop/26.보도자료'

#------------파일 생성하는 코드------------#
def makedirs(path):
   if not os.path.exists(path):
       os.makedirs(path)
       print("폴더 생성")
   else:
       print("이미 같은 이름의 폴더가 생성되어 있습니다.")
#-----------------------------------------#


#--------핵심 단어 입력하는 코드------------#
search_word = input("핵심 단어를 입력하세요(*띄어쓰기 유의*) : ")
print(type(search_word))
#-----------------------------------------#


makedirs(path)
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
#driver = webdriver.Chrome(service = service, options=chrome_options)#이거 주석처리하면 크롬창 실행 안됨


url = 'https://www.asiatoday.co.kr/kn_search.php?sword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# find_all 메소드를 사용하여 태그가 nobr이고 class가 tit인 요소들을 모두 가져옵니다.
ul = soup.select_one('div.news_list_df')
titles = ul.select('dl > dd > a')

link_text_array = []#기사 제목을 담은 배열 선언
for title in titles:
    link_text_array.append(title.text)#배열에 저장
    #print(title.get_text())

link_date_array = [0] * 10
#--------배열 길이만큼 제목만 추출하는 코드---------#
for i in range(len(link_text_array)):
    link_date_array[i] = link_text_array[i][-16:-1]#보도 날짜 저장하는 배열
    s = link_text_array[i]#i번째 내용에 값을 s에 저장
    s = s.lstrip('\n')#왼쪽에 있는 개행문자 제거
    newline_index = s.find('\n')
    substring = s[:newline_index]##제목 끝에 개행문자가 있는데 \n앞에까지 자르기
    link_text_array[i] = substring
    print(substring)#제목 출력

#--------제목에서 일치하는 단어가 있는 탐색---------#
cnt = 0
num = 0#배열의 요소 세는 변수
for i in range(len(link_text_array)):#배열에 길이만큼 반복
    a = link_text_array[i].find(search_word)#배열에 0번째 요소에 있는 문자열중에 search_word변수에 담겨있는 단어가 들어있는지 확인(들어있다 = 양수, 없다 = 음수)
    link_text_array[i] = link_text_array[i].replace(" ","")#배열에 들어있는 제목 띄어쓰기 전부 제거
    b = link_text_array[i].find(search_word)#다시 단어 찾기
    num = num + 1
    if a > -1 or b > -1:#들어있으면 cnt 카운트 
        cnt = cnt + 1
        break
    else:
        continue
print("cnt : ",cnt)
print("num : ", num)    
#--------제목이 일치한다면 스크랩 수행--------------#
if cnt > 0:
    driver = webdriver.Chrome(service = service, options=chrome_options)
    print("입력하신 값이 기사제목에 포함되어 있습니다. 스크랩을 수행합니다.")
    #아시아투데이 주소 이동
    driver.get("https://www.asiatoday.co.kr/kn_search.php?sword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8")
    driver.implicitly_wait(10)
    req = driver.page_source
    if(num == 1):
       driver.find_element(By.XPATH, '//*[@id="section_main"]/div[2]/dl/dd[1]/a').click()#기사 1번째 클릭
       date_v = link_date_array[0]
    elif(num == 2):
       driver.find_element(By.XPATH, '//*[@id="section_main"]/div[2]/dl/dd[2]/a').click()#기사 2번째 클릭
       date_v = link_date_array[1]
    elif(num == 3):
       driver.find_element(By.XPATH, '//*[@id="section_main"]/div[2]/dl/dd[3]/a').click()#기사 3번째 클릭
       date_v = link_date_array[2]
    elif(num == 4):
        driver.find_element(By.XPATH, '//*[@id="section_main"]/div[2]/dl/dd[4]/a').click()#기사 4번째 클릭
        date_v = link_date_array[3]
    elif(num == 5):
        driver.find_element(By.XPATH, '//*[@id="section_main"]/div[2]/dl/dd[5]/a').click()#기사 5번째 클릭
        date_v = link_date_array[4]
    else:
        print("그냥 진행합시다")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,'//*[@id="section_top"]/div/dl/dd/ul/li[8]/a').send_keys(Keys.ENTER)#프린터 버튼 클릭
    print(driver.window_handles)
    #창 전환
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    pag.hotkey('ctrl', 'shift', 'p')# '인쇄'창 열기  
    print('진행중')
    time.sleep(5)
    print_box = pag.getWindowsWithTitle('인쇄')[0]
    print_box.activate()#인쇄창 활성
    time.sleep(2)
    print_button = pag.locateCenterOnScreen('인쇄(p).png')#인쇄 버튼 클릭
    pag.click(print_button)
    #pag.moveTo(987, 885, 0.5)#인쇄하기 대상 클릭으로 이동
    #pag.click()

    time.sleep(3)
    w = pag.getWindowsWithTitle("다음 이름으로 프린터 출력 저장")[0]
    w.activate()#다른이름으로 프린터 저장 활성화
    if w.isMaximized == False: # 현재 최대화가 되지 않았다면
        w.maximize() #최대화

    pag.sleep(2) 
    pyperclip.copy(date_v + " 아시아투데이")
    pag.hotkey("ctrl", "v")#쓰는 칸에 붙여넣기
    pag.moveTo(1751, 1005, 0.5)#저장 버튼으로 이동
    pag.click()  
    time.sleep(5)

    driver.quit()

    #-----------파일 옮기는 코드-----------#
    #shutil.move('C:/Users/User/Documents/230414 아시아투데이.pdf','C:/Users/User/Desktop/26.보도자료/230414 아시아투데이.pdf')
    #--------------------------------------

    print("프로세스 완료")
    print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간 

#제목이 일치하지 않으면 스크랩 수행 안함
else:
    print("제목과 일치하지 않습니다")
   

    