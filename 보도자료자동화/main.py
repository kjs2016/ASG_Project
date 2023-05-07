import 아시아투데이, 충청신문, 온아신문, 온양신문, 아산투데이
from tqdm import tqdm
import time

#---------------핵심단어 입력하는 부분------------------#
while True:
 point = input("핵심 단어를 입력하세요(*전부 붙여쓰세요*) : ")
 if point == "":
   print("아무것도 입력하지 않으셨습니다. 다시입력해주세요")
   continue
 else:
   break
 
func_list = [아시아투데이.asiatoday0, 충청신문.cc1, 온아신문.onanews2, 온양신문.ionyang3, 아산투데이.asnatoday4]#각 모듈의 함수명 저장

num_of_functions = len(func_list)#배열의 길이 저장


result = ""
for i in tqdm(range(num_of_functions)):
   try:
      func_list[i](point)#배열에 있는 함수를 호출
      time.sleep(0.5)  # 로딩바 속도를 조절하기 위한 지연 시간
   except Exception as e:
     print(f"{i}번째 함수 실행 중 오류가 발생했습니다 : {e}")
     continue

