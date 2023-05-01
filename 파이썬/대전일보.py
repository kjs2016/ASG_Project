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
driver.get("http://www.daejonilbo.com/news/articleList.html")
driver.implicitly_wait(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

driver.find_element(By.XPATH,'//*[@id="search"]').send_keys('아산시시설관리공단')
driver.find_element(By.XPATH,'//*[@id="userSearch"]/form/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="section-list"]/ul/li[1]/div/h4/a').click()
#driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="articleViewCon"]/article/header/div[2]/article/section[2]/button[1]').send_keys(Keys.ENTER)
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])  
driver.find_element(By.XPATH,'//*[@id="user-warp"]/div/section/div[1]/button').send_keys(Keys.ENTER)
driver.switch_to.window(driver.window_handles[2])  
driver.find_element(By.XPATH,'//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]').send_keys(Keys.ENTER)
print(driver.window_handles)
#창 전환
#driver.find_element(By.XPATH,'/html/body/div[1]/div/button[1]').send_keys(Keys.ENTER)
print('실행 되냐?')
time.sleep(3)
print('실행 된다')
#driver.switch_to.window(driver.window_handles[0]) 
#driver.close()
time.sleep(3)
pag.moveTo(870, 834, 0.5)
pag.click()
pag.press('down')
time.sleep(0.5)
pag.press('enter')
pag.moveTo(898, 886,0.5)
pag.click()
time.sleep(3)
w = pag.getWindowsWithTitle("다른 이름으로 저장")[0]
w.activate()

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
   w.maximize() #최대화

pag.sleep(1) 
#pag.moveTo(214, 899)#파일명 쓰는 칸으로 이동
#pag.click()
pyperclip.copy("230414 대전일보")
pag.hotkey("ctrl", "v")#쓰는 칸에 붙여넣기
pag.moveTo(1698, 1040, 0.5)#저장 버튼으로 이동
time.sleep(0.5)
pag.click()  
time.sleep(3)

driver.quit() 