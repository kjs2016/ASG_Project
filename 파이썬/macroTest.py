import pyautogui as pag #as 별명
from pynput import mouse

def on_click(x, y, button, pressed):
    print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))


with mouse.Listener(
    on_click=on_click) as listener:
    listener.join()

#coord = []

#def click(x, y, button, pressed):
    #if pressed:
      #  x = int(x)
        #y = int(y)
       # coord.append(x)
       # coord.append(y)
        #print(coord)

#with Listener(on_click = click) as Listener:
     #Listener.join()

#print_btn = pag.position();
#print(print_btn)

