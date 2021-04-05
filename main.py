import re
import keyboard
import time

import tkinter
from tkinter import *

from tkinter import messagebox
from sys import exit

showWindow = True

def getHalfWindowSize(window):
    return int(window.winfo_screenwidth() / 4), int(window.winfo_screenheight() / 4)

def getCoordinate(window, width, height):
    return int((window.winfo_screenwidth() / 2) - (width / 2)), int((window.winfo_screenheight() / 2) - (height / 2))

print('Starting to pre-processing...')

# create a tkinter window
window = tkinter.Tk()

# Init frame
width, height = getHalfWindowSize(window)
x, y = getCoordinate(window, width, height)

# Open window having dimension 100x100
window.geometry(f'{width}x{height}+{x}+{y}')

# to rename the title of the window
window.title("Phần mềm chuyển đổi văn tự")
window.wm_iconbitmap("icon.ico")

window.resizable(False, False)

def on_closing():
    if messagebox.askokcancel("Đóng chương trình", "Bạn muốn thoát chương trình?"):
        window.destroy()
        exit()

window.protocol("WM_DELETE_WINDOW", on_closing)

current_word = ''

strInput = StringVar()

strOutput = StringVar()

tkinter.Label(window, text = "Đây là phần mềm chuyển đổi văn tự").pack()

labelInput = Label(window, text="Bạn đang nhập: ").pack(expand=True)

labelOutputUser = Label(window, textvariable=strInput).pack(expand=True)

labelOutput = Label(window, text="Chuyển tự sang: ").pack(expand=True)

labelOutputUser = Label(window, textvariable=strOutput).pack(expand=True)

button = Button(window, text="Thoát", command=lambda : on_closing())
button.pack(expand=True)

def on_press_key(event):
    global current_word

    if (str(event.name).isdigit() or str(event.name).isalpha()) and len(str(event.name)) == 1:
        strInput.set(strInput.get() + str(event.name))
    else:
        strInput.set('')

    if len(str(event.name)) == 1:
        # check start with u
        if str(event.name) == 'u':
            current_word = str(event.name)
        ### check 'a', following 'u'
        elif str(event.name) == 'a' and current_word == 'u':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ố')
            strOutput.set('uố')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ồ')
            strOutput.set('uồ')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ổ')
            strOutput.set('uổ')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ỗ')
            strOutput.set('uỗ')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ộ')
            strOutput.set('uộ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'ua':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ô')
            strOutput.set('uô')
            current_word = ''
        ### check 'i', following 'ua'
        elif str(event.name) == 'i' and current_word == 'ua':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uai':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'y', following 'ua'
        elif str(event.name) == 'y' and current_word == 'ua':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uay':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'n', following 'ua'
        elif str(event.name) == 'n' and current_word == 'ua':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uan':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'g', following 'uan'
        elif str(event.name) == 'g' and current_word == 'uan':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uang':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'y', following 'u' -> uye
        elif str(event.name) == 'y' and current_word == 'u':
            current_word += str(event.name)
        elif str(event.name) == 'e' and current_word == 'uy':
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iế')
            strOutput.set('uiế')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iề')
            strOutput.set('uiề')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iể')
            strOutput.set('uiể')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iễ')
            strOutput.set('uiễ')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iệ')
            strOutput.set('uiệ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iê')
            strOutput.set('uiê')
            current_word = ''

        # check start with 'i'
        elif str(event.name) == 'i':
            current_word = str(event.name)
        # check 'a', following 'i'
        elif str(event.name) == 'a' and current_word == 'i':
            current_word += str(event.name)
        # check 's' -> iế
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ế')
            strOutput.set('ế')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ề')
            strOutput.set('ề')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ể')
            strOutput.set('ể')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ễ')
            strOutput.set('ễ')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ệ')
            strOutput.set('ệ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ê')
            strOutput.set('ê')
            current_word = ''

        elif str(event.name) == 'q' and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('k')
            strOutput.set('k')
        elif (str(event.name) == 'd' or str(event.name) == 'r') and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('z')
            strOutput.set('z')
        elif str(event.name) == 'x' and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('s')
            strOutput.set('s')
        elif str(event.name) == 'c':
            current_word = str(event.name)

            keyboard.send('backspace')
            keyboard.write('k')
            strOutput.set('k')
        elif str(event.name) == 'h' and current_word == 'c':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('c')
            strOutput.set('c')
            current_word = ''

        # tr
        elif str(event.name) == 't':
            current_word = str(event.name)
        elif str(event.name) == 'r' and current_word == 't':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('c')
            strOutput.set('c')
        ## th
        elif str(event.name) == 'h' and current_word == 't':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('q')
            strOutput.set('q')
        # gi
        elif str(event.name) == 'g':
            current_word = str(event.name)
        elif str(event.name) == 'i' and current_word == 'g':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('z')
            strOutput.set('z')
        # nh
        elif str(event.name) == 'n':
            current_word = str(event.name)
        elif str(event.name) == 'h' and current_word == 'n':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ń')
            strOutput.set('ń')
        # ph
        elif str(event.name) == 'p':
            current_word = str(event.name)
        elif str(event.name) == 'h' and current_word == 'p':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('f')
            strOutput.set('f')
        # kh
        elif str(event.name) == 'k':
            current_word = str(event.name)
        elif str(event.name) == 'h' and current_word == 'k':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('x')
            strOutput.set('x')
        # ng
        elif str(event.name) == 'n':
            current_word = str(event.name)
        elif str(event.name) == 'g' and current_word == 'n':
            current_word += str(event.name) # save for checking ngh

            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('w')
            strOutput.set('w')
        # ngh
        elif str(event.name) == 'h' and current_word == 'ng':
            keyboard.send('backspace') # did check and correct on 'ng'
            current_word = ''
        elif str(event.name) != 'h' and current_word == 'ng':
            current_word = ''

        else:
            current_word = ''

keyboard.on_press(on_press_key)

while True:
    if showWindow:
        window.mainloop()
        showWindow = False
    time.sleep(0.01)
    print('Terminate pre-processing...')
    pass