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
# window.wm_iconbitmap("icon.ico")

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
        strOutput.set('')

    if len(str(event.name)) == 1:
        # check start with u
        if str(event.name) in ['u', 'U']:
            current_word = str(event.name)
        ### check 'a', following 'u'
        elif str(event.name) in ['a', 'A'] and current_word in ['u', 'U']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            if str(event.name).isupper():
                keyboard.write('ố')
                strOutput.set('uố')
            else:
                keyboard.write('ố')
                strOutput.set('uố')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ồ')
            strOutput.set('uồ')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ổ')
            strOutput.set('uổ')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ỗ')
            strOutput.set('uỗ')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ộ')
            strOutput.set('uộ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['ua', 'UA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ô')
            strOutput.set('uô')
            current_word = ''
        ### check 'i', following 'ua'
        elif str(event.name) in ['i', 'I'] and current_word in ['ua', 'UA']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['uai', 'UAI']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'y', following 'ua'
        elif str(event.name) in ['y', 'Y'] and current_word in ['ua', 'UA']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['uay', 'UAY']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'n', following 'ua'
        elif str(event.name) in ['n', 'N'] and current_word in ['ua', 'UA']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['uan', 'UAN']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'g', following 'uan'
        elif str(event.name) in ['g', 'G'] and current_word in ['uan', 'UAN']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('á')
            strOutput.set('uá')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('à')
            strOutput.set('uà')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ả')
            strOutput.set('uả')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ã')
            strOutput.set('uã')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ạ')
            strOutput.set('uạ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['uang', 'UANG']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('a')
            strOutput.set('ua')
            current_word = ''
        ### check 'y', following 'u' -> uye
        elif str(event.name) in ['y', 'Y'] and current_word in ['u', 'U']:
            current_word += str(event.name)
        elif str(event.name) in ['e', 'E'] and current_word in ['uy', 'UY']:
            current_word += str(event.name)
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iế')
            strOutput.set('uiế')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iề')
            strOutput.set('uiề')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iể')
            strOutput.set('uiể')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iễ')
            strOutput.set('uiễ')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iệ')
            strOutput.set('uiệ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['uye', 'UYE']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iê')
            strOutput.set('uiê')
            current_word = ''

        # check start with 'i'
        elif str(event.name) in ['i', 'I']:
            current_word = str(event.name)
        # check 'a', following 'i'
        elif str(event.name) in ['a', 'A'] and current_word in ['i', 'I']:
            current_word += str(event.name)
        # check 's' -> iế
        elif (str(event.name) in ['s', 'S'] or str(event.name) == '1') and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ế')
            strOutput.set('ế')
            current_word = ''
        elif (str(event.name) in ['f', 'F'] or str(event.name) == '2') and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ề')
            strOutput.set('ề')
            current_word = ''
        elif (str(event.name) in ['w', 'W'] or str(event.name) == '3') and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ể')
            strOutput.set('ể')
            current_word = ''
        elif (str(event.name) in ['o', 'O'] or str(event.name) == '4') and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ễ')
            strOutput.set('ễ')
            current_word = ''
        elif (str(event.name) in ['j', 'J'] or str(event.name) == '5') and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ệ')
            strOutput.set('ệ')
            current_word = ''
        elif str(event.name) == '=' and current_word in ['ia', 'IA']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ê')
            strOutput.set('ê')
            current_word = ''

        elif str(event.name) in ['q', 'Q'] and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('k')
            strOutput.set('k')
        elif (str(event.name) in ['d', 'D'] or str(event.name) in ['r', 'R']) and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('z')
            strOutput.set('z')
        elif str(event.name) in ['x', 'X'] and len(current_word) == 0:
            keyboard.send('backspace')
            keyboard.write('s')
            strOutput.set('s')
        elif str(event.name) in ['c', 'C']:
            current_word = str(event.name)

            keyboard.send('backspace')
            keyboard.write('k')
            strOutput.set('k')
        elif str(event.name) in ['h', 'H'] and current_word in ['c', 'C']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('c')
            strOutput.set('c')
            current_word = ''

        # tr
        elif str(event.name) in ['t', 'T']:
            current_word = str(event.name)
        elif str(event.name) in ['r', 'R'] and current_word in ['t', 'T']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('c')
            strOutput.set('c')
        ## th
        elif str(event.name) in ['h', 'H'] and current_word in ['t', 'T']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('q')
            strOutput.set('q')
        # gi
        elif str(event.name) in ['g', 'G']:
            current_word = str(event.name)
        elif str(event.name) in ['i', 'I'] and current_word in ['g', 'G']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('z')
            strOutput.set('z')
        # nh
        elif str(event.name) in ['n', 'N']:
            current_word = str(event.name)
        elif str(event.name) in ['h', 'H'] and current_word in ['n', 'N']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ń')
            strOutput.set('ń')
        # ph
        elif str(event.name) in ['p', 'P']:
            current_word = str(event.name)
        elif str(event.name) in ['h', 'H'] and current_word in ['p', 'P']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('f')
            strOutput.set('f')
        # kh
        elif str(event.name) in ['k', 'K']:
            current_word = str(event.name)
        elif str(event.name) in ['h', 'H'] and current_word in ['k', 'K']:
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('x')
            strOutput.set('x')
        # ng
        elif str(event.name) in ['n', 'N']:
            current_word = str(event.name)
        elif str(event.name) in ['g', 'G'] and current_word in ['n', 'N']:
            current_word += str(event.name) # save for checking ngh

            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('w')
            strOutput.set('w')
        # ngh
        elif str(event.name) in ['h', 'H'] and current_word in ['ng', 'NG']:
            keyboard.send('backspace') # did check and correct on 'ng'
            current_word = ''
        elif str(event.name) not in ['h', 'H'] and current_word in ['ng', 'NG']:
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