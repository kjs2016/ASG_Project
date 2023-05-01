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
import shutil
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.

def print_click():
    pag.moveTo(1228, 841)
    pag.click()  

start = time.time()
path = 'C:/Users/eksld/Desktop/26.보도자료'
#os.mkdir(path)  
#print("파일 생성")
def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("폴더 생성")
    else:
        print("이미 같은 이름의 폴더가 생성되어 있습니다.")

makedirs(path)
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
driver = webdriver.Chrome(service = service, options=chrome_options)



#신문사 주소 이동
driver.get("https://www.asiatoday.co.kr/kn_search.php?sword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8")
driver.implicitly_wait(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

driver.find_element(By.XPATH,'//*[@id="section_main"]/div[2]/dl/dd[1]/a').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="section_top"]/div/dl/dd/ul/li[8]/a').send_keys(Keys.ENTER)
print(driver.window_handles)
#창 전환
driver.switch_to.window(driver.window_handles[1])
pag.hotkey('ctrl', 'shift', 'p')# '인쇄'창 열기  
print('진행중')
time.sleep(5)
print_box = pag.getWindowsWithTitle('인쇄')[0]
print_box.activate()#인쇄창 활성
print_button = pag.locateCenterOnScreen('인쇄(p).PNG')#인쇄 버튼 클릭
pag.click(print_button)
pag.moveTo(987, 885, 0.5)#인쇄하기 대상 클릭으로 이동
pag.click()

time.sleep(8)
w = pag.getWindowsWithTitle("다음 이름으로 프린터 출력 저장")[0]
w.activate()#다른이름으로 프린터 저장 활성화
if w.isMaximized == False: # 현재 최대화가 되지 않았다면
   w.maximize() #최대화

pag.sleep(2) 
pyperclip.copy("230414 아시아투데이")
pag.hotkey("ctrl", "v")#쓰는 칸에 붙여넣기
pag.moveTo(1698, 1040, 0.5)#저장 버튼으로 이동
pag.click()  
time.sleep(5)

driver.quit()
shutil.move('C:/Users/eksld/OneDrive/문서/230414 아시아투데이.pdf','C:/Users/eksld/Desktop/26.보도자료/230414 아시아투데이.pdf')
print("프로세스 완료")
print(f"{time.time()-start:.4f} sec")#현재시간 - 시작시간 = 실행시간 