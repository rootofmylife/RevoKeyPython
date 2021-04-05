import re
import keyboard
import time

import tkinter
from tkinter import *

from tkinter import messagebox
from sys import exit

showWindow = True

def getHalfWindowSize(window):
    return int(window.winfo_screenwidth() / 2) + 250, int(window.winfo_screenheight() / 1)

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

def on_closing():
    if messagebox.askokcancel("Đóng chương trình", "Bạn muốn thoát chương trình?"):
        window.destroy()
        exit()

window.protocol("WM_DELETE_WINDOW", on_closing)

keyboard.remap_key('q', 'k')
keyboard.remap_key('d', 'z')
keyboard.remap_key('r', 'z')
keyboard.remap_key('x', 's')
keyboard.remap_key('c', 'k')

keyboard.add_abbreviation('tz', 'c') # tr -> c
keyboard.add_abbreviation('gi', 'z')
keyboard.add_abbreviation('nh', 'ń')
keyboard.add_abbreviation('ph', 'f')
keyboard.add_abbreviation('kh', 'x')
keyboard.add_abbreviation('th', 'q')
keyboard.add_abbreviation('kkh', 'c') # ch -> c
keyboard.add_abbreviation('ng', 'w')
keyboard.add_abbreviation('ngh', 'w')

# ia -> iê
# keyboard.add_abbreviation('ia', 'iê', match_suffix=True)
# VNI
# keyboard.add_abbreviation('iaf', 'iề', match_suffix=True)
# keyboard.add_abbreviation('ias', 'iế', match_suffix=True)
# keyboard.add_abbreviation('iar', 'iể', match_suffix=True)
# keyboard.add_abbreviation('iax', 'iễ', match_suffix=True)
# keyboard.add_abbreviation('iaj', 'iệ', match_suffix=True)
# Telex
# keyboard.add_abbreviation('ia2', 'iề', match_suffix=True)
# keyboard.add_abbreviation('ia1', 'iế', match_suffix=True)
# keyboard.add_abbreviation('ia3', 'iể', match_suffix=True)
# keyboard.add_abbreviation('ia4', 'iễ', match_suffix=True)
# keyboard.add_abbreviation('ia5', 'iệ', match_suffix=True)

# ua -> uô
keyboard.add_abbreviation('ua', 'uô', match_suffix=True)
# VNI
keyboard.add_abbreviation('uaf', 'uồ', match_suffix=True)
keyboard.add_abbreviation('uas', 'uố', match_suffix=True)
keyboard.add_abbreviation('uar', 'uổ', match_suffix=True)
keyboard.add_abbreviation('uax', 'uỗ', match_suffix=True)
keyboard.add_abbreviation('uaj', 'uộ', match_suffix=True)
# VNI
keyboard.add_abbreviation('ua2', 'uồ', match_suffix=True)
keyboard.add_abbreviation('ua1', 'uố', match_suffix=True)
keyboard.add_abbreviation('ua3', 'uổ', match_suffix=True)
keyboard.add_abbreviation('ua4', 'uỗ', match_suffix=True)
keyboard.add_abbreviation('ua5', 'uộ', match_suffix=True)

# uye -> uie
keyboard.add_abbreviation('uye', 'uiê', match_suffix=True)
# VNI
keyboard.add_abbreviation('uyef', 'uiề', match_suffix=True)
keyboard.add_abbreviation('uyes', 'uiế', match_suffix=True)
keyboard.add_abbreviation('uyer', 'uiể', match_suffix=True)
keyboard.add_abbreviation('uyex', 'uiễ', match_suffix=True)
keyboard.add_abbreviation('uyej', 'uiệ', match_suffix=True)
# Telex
keyboard.add_abbreviation('uye2', 'uiề', match_suffix=True)
keyboard.add_abbreviation('uye1', 'uiế', match_suffix=True)
keyboard.add_abbreviation('uye3', 'uiể', match_suffix=True)
keyboard.add_abbreviation('uye4', 'uiễ', match_suffix=True)
keyboard.add_abbreviation('uye5', 'uiệ', match_suffix=True)

# uan -> ua
keyboard.add_abbreviation('uan', 'ua', match_suffix=True)
# VNI
keyboard.add_abbreviation('uanf', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uans', 'úa', match_suffix=True)
keyboard.add_abbreviation('uanr', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uanx', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uanj', 'ụa', match_suffix=True)
# Telex
keyboard.add_abbreviation('uan2', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uan1', 'úa', match_suffix=True)
keyboard.add_abbreviation('uan3', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uan4', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uan5', 'ụa', match_suffix=True)

# uang -> ua
keyboard.add_abbreviation('uang', 'ua', match_suffix=True)
# VNI
keyboard.add_abbreviation('uangf', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uangs', 'úa', match_suffix=True)
keyboard.add_abbreviation('uangr', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uangx', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uangj', 'ụa', match_suffix=True)
# Telex
keyboard.add_abbreviation('uang2', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uang1', 'úa', match_suffix=True)
keyboard.add_abbreviation('uang3', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uang4', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uang5', 'ụa', match_suffix=True)

# uai -> ua
keyboard.add_abbreviation('uai', 'ua', match_suffix=True)
# VNI
keyboard.add_abbreviation('uaif', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uais', 'úa', match_suffix=True)
keyboard.add_abbreviation('uair', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uaix', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uaij', 'ụa', match_suffix=True)
# Telex
keyboard.add_abbreviation('uai2', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uai1', 'úa', match_suffix=True)
keyboard.add_abbreviation('uai3', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uai4', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uai5', 'ụa', match_suffix=True)

# uay -> ua
keyboard.add_abbreviation('uay', 'ua', match_suffix=True)
# VNI
keyboard.add_abbreviation('uayf', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uays', 'úa', match_suffix=True)
keyboard.add_abbreviation('uayr', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uayx', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uayj', 'ụa', match_suffix=True)
# Telex
keyboard.add_abbreviation('uay2', 'ùa', match_suffix=True)
keyboard.add_abbreviation('uay1', 'úa', match_suffix=True)
keyboard.add_abbreviation('uay3', 'ủa', match_suffix=True)
keyboard.add_abbreviation('uay4', 'ũa', match_suffix=True)
keyboard.add_abbreviation('uay5', 'ụa', match_suffix=True)

current_word = ''

def on_press_key(event):
    global current_word

    if len(str(event.name)) == 1:
        # check start with u
        if str(event.name) == 'u':
            current_word = str(event.name)
        ### check 'a', following 'u'
        elif str(event.name) == 'a' and current_word == 'u':
            current_word += str(event.name)
        # check 'i', following 'ua'
        elif str(event.name) == 'i' and current_word == 'ua':
            current_word += str(event.name)
        # check 'y', following 'ua'
        elif str(event.name) == 'y' and current_word == 'ua':
            current_word += str(event.name)
        # check 'n', following 'ua'
        elif str(event.name) == 'n' and current_word == 'ua':
            current_word += str(event.name)
        # check 'g', following 'uan'
        elif str(event.name) == 'g' and current_word == 'uan':
            current_word += str(event.name)
        ### check 'y', following 'u'
        elif str(event.name) == 'y' and current_word == 'u'
            current_word += str(event.name)
        elif str(event.name) == 'e' and current_word == 'uy'
            current_word += str(event.name)
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iế')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iề')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iể')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iễ')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iệ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'uye':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('iê')
            current_word = ''

        # check start with 'i'
        if str(event.name) == 'i':
            current_word = str(event.name)
        # check 'a', following 'i'
        elif str(event.name) == 'a' and current_word == 'i':
            current_word += str(event.name)
        # check 's' -> iế
        elif (str(event.name) == 's' or str(event.name) == '1') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ế')
            current_word = ''
        elif (str(event.name) == 'f' or str(event.name) == '2') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ề')
            current_word = ''
        elif (str(event.name) == 'w' or str(event.name) == '3') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ể')
            current_word = ''
        elif (str(event.name) == 'o' or str(event.name) == '4') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ễ')
            current_word = ''
        elif (str(event.name) == 'j' or str(event.name) == '5') and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ệ')
            current_word = ''
        elif str(event.name) == '=' and current_word == 'ia':
            keyboard.send('backspace')
            keyboard.send('backspace')
            keyboard.write('ê')
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