from pprint import pprint as pp
a = {"충청신문"
     : "https://www.dailycc.net/news/articleList.html?sc_area=A&view_type=sm&sc_word=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8",
       "온아신문"
     : "http://www.onanews.net/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=%EC%95%84%EC%82%B0%EC%8B%9C%EC%8B%9C%EC%84%A4%EA%B4%80%EB%A6%AC%EA%B3%B5%EB%8B%A8&imageField.x=0&imageField.y=0"}

for key in a.keys():
      print(key)