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
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.

def print_click():
    pag.moveTo(1228, 841)
    pag.click()  
    


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
driver = webdriver.Chrome(service = service, options=chrome_options)



# 충청신문 주소 이동
#driver.get("https://prt.cctoday.co.kr/engine_yonhap/search.php?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&_ga=2.211558610.658557104.1682583195-73037611.1681804658")
driver.get("http://www.onanews.net/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&imageField.x=0&imageField.y=0")
driver.implicitly_wait(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

driver.find_element(By.XPATH,'//*[@id="search_result"]/div[2]/div[1]/dl/dt/a').click()
#driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="wrap"]/table/tbody/tr/td[1]/div[8]/div[3]/ul/li[1]/a').send_keys(Keys.ENTER)
#time.sleep(5)
print(driver.window_handles)
#창 전환
driver.switch_to.window(driver.window_handles[1])
pag.hotkey('ctrl', 'shift', 'p')
print('실행 되나요?')
time.sleep(0.5)
print('실행 됩니다.')
time.sleep(0.5)
pag.moveTo(941, 817, 0.5)
pag.click()
time.sleep(2)
w = pag.getWindowsWithTitle("다음 이름으로 프린터 출력 저장")[0]
w.activate()
if w.isMaximized == False: # 현재 최대화가 되지 않았다면
  w.maximize() #최대화

time.sleep(1) 
#pag.moveTo(214, 899)#파일명 쓰는 칸으로 이동
#pag.click()
#pag.dragRel(-30, 0, 2, button='left')#윈쪽으로 드래그
pyperclip.copy("230418 온아신문")
pag.hotkey("ctrl", "v")#쓰는 간에 붙여넣기
pag.moveTo(1698, 1040, 1)#저장 버튼으로 이동
time.sleep(1)
pag.click()  
time.sleep(2.5)

driver.quit() 
print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간
