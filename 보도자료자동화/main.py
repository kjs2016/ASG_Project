import 아시아투데이, 충청신문, 온아신문, 온양신문, 아산투데이, 아산시사신문, 온주신문, C뉴스041, 뉴스세상, 로컬투데이, 아산포커스, 충청투데이
import 대전투데이, 충청매일, 충청일보, 동양일보, 충청타임즈, 금강일보, 충남신문, 디트뉴스, 천지일보, 대전일보, 중앙매일, 충남일보
import 백제뉴스, 충청뉴스, 아산데스크, 아산데일리, 아산미래신문, 아산뉴스, 충남타임즈, 뉴스충청인, 투데이충남, 온양뉴스, 내일신문
import 아산in, 배방신문, 농수축산신문, 뉴스타운, 굿모닝충청, 충남in, 중부매일, IPTV뉴스
from tqdm import tqdm
import time
import sys
import traceback


def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open("Log.txt", "a") as f:
        f.write(f"[{current_time}] - {error}\n")

#---------------핵심단어 입력하는 부분------------------#
while True:
 point = input("핵심 단어를 입력하세요(*전부 붙여쓰세요*) : ")
 if point == "":
   print("아무것도 입력하지 않으셨습니다. 다시입력해주세요")
   continue
 else:
   break
 
func_list = [아산포커스.asanfocus10, 아산데일리.asandaily27, 아시아투데이.asiatoday0, 충청신문.cc1, 온아신문.onanews2, 온양신문.ionyang3, 아산투데이.asnatoday4, 아산시사신문.asansisa5,
             온주신문.onjoo6, C뉴스041.cnews041_7, 뉴스세상.newssesang8, 로컬투데이.localtoday9, 아산포커스.asanfocus10,
             충청투데이.cctoday11, 대전투데이.daejeontoday12, 충청매일.ccdn13, 충청일보.ccdailynews14, 동양일보.dynews15, 충청타임즈.cctimes16, 금강일보.ggilbo17, 충남신문.ccsimin18, 디트뉴스.dtnews24_19
             , 천지일보.newscj20, 대전일보.daejonilbo21, 중앙매일.jamill22, 충남일보.chungnamilbo23, 백제뉴스.ebaekje24, 충청뉴스.ccnnews25, 아산데스크.asandesk26
             , 아산데일리.asandaily27, 아산미래신문.asanmiraenews28, 아산뉴스.asannews29, 충남타임즈.cntimes30, 뉴스충청인.cndnews31, 투데이충남.todaychungnam32, 온양뉴스.onyangnews33,
             내일신문.naeil34, 아산in.asanin35, 배방신문.baebang36, 농수축산신문.aflnews37, 뉴스타운.newstown38, 굿모닝충청.goodmorningcc39,
             충남in.chungnamin40, 중부매일.jbnews41, IPTV뉴스.iptvnews42]#각 모듈의 함수명 저장

num_of_functions = len(func_list)#배열의 길이 저장



"""
result = ""
for i in tqdm(range(num_of_functions)):
   try:
      func_list[i](point)#배열에 있는 함수를 호출
      time.sleep(0.5)  # 로딩바 속도를 조절하기 위한 지연 시간
   except Exception as e:
     print(f"{i}번째 함수 실행 중 오류가 발생했습니다 : {e}")
     continue
"""
errors = []
for i in tqdm(range(num_of_functions), file=sys.stdout):
   try:
      func_list[i](point)  # 배열에 있는 함수를 호출
      time.sleep(0.5)  # 로딩바 속도를 조절하기 위한 지연 시간
   except Exception as e:
      errors.append((i, e))
      err = traceback.format_exc()
      ErrorLog(str(err))

if errors:
   print("오류가 발생한 함수:")
   for i, e in errors:
      print(f"{i}번째 함수 실행 중 오류가 발생했습니다 : {e}")
else:
   print("오류가 발생하지 않았습니다.")

