from tkinter import *

win = Tk() #창 생성

win.geometry("500x500")
win.title("ASG News Scraper")
win.option_add("*Font","맑은고딕 25")#폰트 처리
#win.configure(bg='black')

btn = Button(win, text="버튼")
#btn = config(width = 20, height=20)
btn.pack()

win.mainloop() # 창 실행