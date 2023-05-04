import requests
from bs4 import BeautifulSoup

search_word = input("핵심 단어를 입력하세요(*띄어쓰기 유의*) : ")
print(type(search_word))

url = 'https://www.asiatoday.co.kr/kn_search.php?sword=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#section_main > div.news_list_df > dl > dd:nth-child(1) > a > h5')
    #print(title.get_text())
    NewsTitle = title.get_text()
    #NewsTitle = NewsTitle.replace(" ","")#공백을 제거하는 함수
    #print(NewsTitle)
else : 
    print(response.status_code)

a = NewsTitle.find(search_word)
print(type(a))
print(NewsTitle.find('야호'))
