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

def Print_Control(input1, input2):
    pag.hotkey('ctrl', 'shift', 'p')
    #driver.find_element(By.XPATH,'//*[@id="user-warp"]/div/section/div[4]/button').send_keys(Keys.ENTER)#인쇄버튼 클릭
    print('실행 되나요?')
    time.sleep(0.5)
    print('실행 됩니다.')
    time.sleep(6)
    print_box = pag.getWindowsWithTitle('인쇄')[0]
    print_box.activate()
    print_button = pag.locateCenterOnScreen('인쇄(p).PNG')
    pag.click(print_button)
    """
    time.sleep(0.5)
    pag.moveTo(941, 817, 0.5)
    pag.click()
    time.sleep(2)
    """
    time.sleep(10)
    w = pag.getWindowsWithTitle("다음 이름으로 프린터 출력 저장")[0]
    w.activate()
    if w.isMaximized == False: # 현재 최대화가 되지 않았다면
        w.maximize() #최대화
    if input1 != "":
        pyperclip.copy(input1+" "+input2)
    else:
        pyperclip.copy(input2)
    pag.hotkey("ctrl", "v")#쓰는 간에 붙여넣기
    pag.moveTo(1698, 1040, 1)#저장 버튼으로 이동
    time.sleep(2)
    pag.click()  

