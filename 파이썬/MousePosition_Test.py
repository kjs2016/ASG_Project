import pyautogui as pag #as 별명
from pynput import mouse
import win32api as win32
import time


while True:
    # win32 api로 마우스의 상태를 가져옵니다.
    down = win32.GetKeyState(0x01)
    # 마우스 상태가 다운이면 와일문을 탈출합니다.
    if down == 0:
        break
    # 마우스의 현재 좌표를 출력합니다.
    print(pag.position())
    time.sleep(2)
