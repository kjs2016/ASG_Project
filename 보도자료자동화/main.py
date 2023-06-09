import 아시아투데이, 충청신문, 온아신문, 온양신문, 아산투데이, 아산시사신문, 온주신문, C뉴스041, 뉴스세상, 로컬투데이, 아산포커스, 충청투데이
import 대전투데이, 충청매일, 충청일보, 동양일보, 충청타임즈, 금강일보, 충남신문, 디트뉴스, 천지일보, 대전일보, 중앙매일, 충남일보
import 백제뉴스, 충청뉴스, 아산데스크, 아산데일리, 아산미래신문, 아산뉴스, 충남타임즈, 뉴스충청인, 투데이충남, 온양뉴스, 내일신문
import 아산in, 배방신문, 농수축산신문, 뉴스타운, 굿모닝충청, 충남in, 중부매일, IPTV뉴스
from tqdm import tqdm
import time
import sys
import traceback
import tkinter as tk
from tkinter import messagebox
import threading

errors = []
sum = 0

func_list = [아시아투데이.asiatoday0, 충청신문.cc1, 온아신문.onanews2, 온양신문.ionyang3, 아산투데이.asnatoday4, 아산시사신문.asansisa5,
             온주신문.onjoo6, C뉴스041.cnews041_7, 뉴스세상.newssesang8, 로컬투데이.localtoday9, 아산포커스.asanfocus10,
             충청투데이.cctoday11, 대전투데이.daejeontoday12, 충청매일.ccdn13, 충청일보.ccdailynews14, 동양일보.dynews15, 충청타임즈.cctimes16, 금강일보.ggilbo17, 충남신문.ccsimin18, 디트뉴스.dtnews24_19
             , 천지일보.newscj20, 대전일보.daejonilbo21, 중앙매일.jamill22, 충남일보.chungnamilbo23, 백제뉴스.ebaekje24, 충청뉴스.ccnnews25, 아산데스크.asandesk26
             , 아산데일리.asandaily27, 아산미래신문.asanmiraenews28, 아산뉴스.asannews29, 충남타임즈.cntimes30, 뉴스충청인.cndnews31, 투데이충남.todaychungnam32, 온양뉴스.onyangnews33,
             내일신문.naeil34, 아산in.asanin35, 배방신문.baebang36, 농수축산신문.aflnews37, 뉴스타운.newstown38, 굿모닝충청.goodmorningcc39,
             충남in.chungnamin40, 중부매일.jbnews41, IPTV뉴스.iptvnews42]#각 모듈의 함수명 저장
point =""
file_name=""


def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open("Log.txt", "a") as f:
        f.write(f"[{current_time}] - {error}\n")

num_of_functions = len(func_list)#배열의 길이 저장

def start_scrap(point):
  global sum
   word = point
   for i in tqdm(range(num_of_functions), file=sys.stdout):
      try:
         func_list[i](word)  # 배열에 있는 함수를 호출
         time.sleep(0.5)  # 로딩바 속도를 조절하기 위한 지연 시간
         pb["value"] = i
         pb.update()
         num = func_list[i](word)
         sum = sum + num
         if i >= num_of_functions-1:
            label2.config(text="스크랩이 완료되었습니다")
            button.config(text='확인')
            button.configure(bg='#4aa8d8')
            messagebox.showwarning("알림", f"{sum}개의 스크랩을 수행하였습니다")
            if errors:
               print("오류가 발생한 함수:")
               for i, e in errors:
                   print(f"{i}번째 함수 실행 중 오류가 발생했습니다 : {e}")
            else:
               print("오류가 발생하지 않았습니다.") 
      except Exception as e:
         errors.append((i, e))
         err = traceback.format_exc()
         ErrorLog(str(err))


def show_warning():
   messagebox.showwarning("경고", "값을 입력하지 않았습니다. 값을 입력해주세요")

def on_close():
    if messagebox.askokcancel("확인", "프로그램을 종료하시겠습니까?"):
        root.destroy()   
        
#확인 버튼을 누르면 함수가 실행된다.
def on_button_click():
    point = entry.get()
    file_name = entry_file.get()
    if not point:
      show_warning()
    else:
      label.config(text="스크랩이 진행중입니다")
      button.config(text='진행중')
      button.configure(bg='#A0D468')
      entry.delete(0, tk.END)
      #배열에 들어있는 뉴스기사를 순차적으로 실행
      thread = threading.Thread(target=start_scrap, args=(point,))
      thread.daemon = True
      thread.start()

      #num_of_functions = len(func_list)#배열의 길이 저장
      #for i in tqdm(range(num_of_functions), file=sys.stdout):
         #try:
            #func_list[i](point)  # 배열에 있는 함수를 호출
            #time.sleep(0.5)  # 로딩바 속도를 조절하기 위한 지연 시간
         #except Exception as e:
            #errors.append((i, e))
            ##err = traceback.format_exc()
            #ErrorLog(str(err))
      


#엔터를 누르면 스크랩이 수행되는 부분
def enter_pressed(event):
    on_button_click()
            
#------------유의사항 창-----------#
def new_window():
   add_window = tk.Toplevel(root)
   #add_window.geometry("700x150")
   add_window.title("유의사항")

   label = tk.Label(add_window, text="1. 핵심단어는 띄어쓰기 x", font=("맑은 고딕", '12'))
   label.pack(padx=20, pady=30)

   label = tk.Label(add_window, text="2. 핵심단어는 기사 제목에 반드시 포함되고 다른 기사제목과 중복되지 않는걸로 입력", font=("맑은 고딕",'12'))
   label.pack(padx=20)
   label = tk.Label(add_window, text=" *피해야 될 단어 예시 : 아산시시설관리공단, 영인산박물관, 곤충원 등등", font=("맑은 고딕",'12'))
   label.pack(padx=20)

   label = tk.Label(add_window, text="3. 실행도중에 종료하면 생성된 pdf 파일을 전부 제거후 다시 실행", font=("맑은 고딕",'12'))
   label.pack(padx=20, pady=30)
#----------------------------------------#
    #print("입력된 단어:", input_text)
if __name__ == "__main__":
   root = tk.Tk()

   root.title('ANS')
  
   # Menu 생성
   menubar = tk.Menu(root)

   # 일반 메뉴 콘텐츠 작성
   helpmenu = tk.Menu(menubar, tearoff=0)
   helpmenu.add_command(label="유의사항", command=new_window)
   helpmenu.add_command(label="정보", command=None)
   menubar.add_cascade(label="메뉴", menu=helpmenu)

   root.config(menu=menubar)
  
   image = tk.PhotoImage(file="C:/Users/eksld/Desktop/Asg_Project/ASG_Project-2/보도자료자동화/아산시시설관리공단1.png")
   # 이미지 삽입
   label1 = tk.Label(image=image)
   #label1.grid(row=0, column=0, padx=30,pady=10)
   label1.pack()
    
   # Progress Bar 생성
   pb = tkinter.ttk.Progressbar(root, maximum=num_of_functions-1, length = 300)
   pb.pack()
    

   label = tk.Label(root, text="핵심단어를 입력하세요!", font=("Arial", 20))
   label.pack()

   entry = tk.Entry(root, font=("Arial", 20))
   entry.pack()
    
   #-----------------파일명 입력받는 곳--------------------------#
   label3 = tk.Label(root, text="파일명을 입력하세요!", font=("Arial", 20))
   #label2.grid(row=1, column=0, padx=30,pady=10)
   label3.pack()

   entry_file = tk.Entry(root, font=("Arial", 20))
   #entry.grid(row=2, column=0, padx=5,pady=10)
   entry_file.pack()
   #------------------------------------------------------------#

   button = tk.Button(root, text="확인", command=on_button_click, font=("Arial", 15), bg='#4aa8d8')
   button.pack(side=tk.LEFT, padx=50)

   exit_button = tk.Button(root, text="종료", command=on_close,  font=("Arial", 15), bg='#f05650')
   exit_button.pack(side=tk.LEFT, padx=60)

   root.bind('<Return>', enter_pressed)

   root.mainloop()
