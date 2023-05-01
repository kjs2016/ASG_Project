import pyautogui as pag
import time
import os
import shutil

fw = pag.getActiveWindow()
print(fw.title)

for w in pag.getAllWindows():
   print(w)

#폴더 생성 코드
path = 'C:/Users/eksld/Desktop/26.보도자료'
#os.mkdir(path)  

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("폴더 생성")
    else:
        print("이미 같은 이름의 폴더가 생성되어 있습니다.")

makedirs(path)
shutil.move('C:/Users/eksld/Downloads/230418 온아신문.pdf','C:/Users/eksld/Desktop/26.보도자료/230418 온아신문.pdf')
"""
print_box = pag.getWindowsWithTitle('인쇄')[0]
print_box.activate()/

print_button = pag.locateCenterOnScreen('인쇄(p).PNG')
pag.click(print_button)
#w = pyautogui.getWindowsWithTitle("다른 이름으로 저장")[0]
#print(w)
#w.activate()

#if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    #w.maximize() #최대화

"""