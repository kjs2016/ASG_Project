import requests
from bs4 import BeautifulSoup

while True:
 point = input("핵심 단어를 입력하세요(*전부 붙여쓰세요*) : ")
 if point == "":
   print("아무것도 입력하지 않으셨습니다. 다시입력해주세요")
   continue
 else:
   break
 
search_word = point


url = "http://www.daejonilbo.com/news/articleList.html"

headers = {
    "Referer" : "http://www.daejonilbo.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

data = {
    "sc_area": "A",
    "view_type": "sm",
    "sc_word": "아산시시설관리공단"   
}
res = requests.post(url, headers = headers, data=data)
print(res.text)

soup = BeautifulSoup(res.text, "lxml")
search_results = soup.find_all("h4", class_="titles line-6x3")

new_title_array=[]#기사 제목을 담을 배열 선언

    # 선택된 모든 div 태그에 대해 a 태그 검색
for result in search_results:
    a_tags = result.find_all("a")
    for tag in a_tags:
        new_title_array.append(tag.text)

#배열 요소와 값 함께 출력
for i, item in enumerate(new_title_array):
    print(i, item)

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
       # break
    else:
        continue
print("cnt : ",cnt)
print("num : ", num)