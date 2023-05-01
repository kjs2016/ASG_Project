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
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path = ChromeDriverManager().install())#크롬 드라이버 최신 버전 자동 설치
driver = webdriver.Chrome(service = service, options=chrome_options)

# 충청신문 주소 이동
#driver.get("https://prt.cctoday.co.kr/engine_yonhap/search.php?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&_ga=2.211558610.658557104.1682583195-73037611.1681804658")
driver.get("https://www.dailycc.net/news/articleList.html?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8")
driver.implicitly_wait(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

driver.find_element(By.XPATH,'//*[@id="section-list"]/ul/li[1]/h4/a').click()
#driver.find_element(By.XPATH,'//*[@id="search_result"]/div[1]/div[2]/div[1]/div[2]/div/a').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="articleViewCon"]/article/article[2]/button[7]').send_keys(Keys.ENTER)
#time.sleep(5)
print(driver.window_handles)
#창 전환
driver.switch_to.window(driver.window_handles[-1])  
driver.find_element(By.XPATH,'//*[@id="user-warp"]/div/section/div[4]/button').send_keys(Keys.ENTER)
#driver.find_element(By.XPATH,'//*[@id="articleViewCon"]/article/div[2]/article[2]/a[2]').click()
#기사 목록 가져오는 코드
#member = driver.find_elements(By.CLASS_NAME, 'news_list_df')
#member = driver.find_elements(By.TAG_NAME, 'dd')[1]
#member = driver.find_elements(By.TAG_NAME,'a')


#for name in member:
   #print(name.text)