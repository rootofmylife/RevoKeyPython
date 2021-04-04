import re
import unidecode
import keyboard

from tkinter import *

mapping_scheme = {
    'c': 'k',
    'q': 'k',
    'd': 'z',
    'gi': 'z',
    'r': 'z',
    'ch': 'c',
    'tr': 'c',
    'ng': 'w',
    'ngh': 'w',
    'nh': 'ń',
    'ph': 'f',
    'kh': 'x',
    'x': 's',
    'th': 'q',
    'ia': 'iê', 'ìa': 'iề', 'ía': 'iế', 'ỉa': 'iể', 'ĩa': 'iễ', 'ịa': 'iệ',
    'uan': 'ua', 'uản': 'ủa', 'uàn': 'ùa', 'uán': 'úa', 'uãn': 'ũa', 'uạn': 'ụa',
    'uang': 'ua', 'uàng': 'ùa', 'uáng': 'úa', 'uảng': 'ủa', 'uãng': 'ũa', 'uạng': 'ụa',
    'uai': 'ua', 'uài': 'ùa', 'uái': 'úa', 'uại': 'ụa', 'uải': 'ủa', 'uãi': 'ũa',
    'uay': 'ua', 'uày': 'ùa', 'uáy': 'úa', 'uạy': 'ụa', 'uảy': 'ủa', 'uãy': 'ũa',
    'ua': 'uô', # end of morpho
    'úa': 'uố', 'ùa': 'uồ', 'ủa': 'uổ', 'ũa': 'uỗ', 'ụa': 'uộ',
    'uyê': 'uiê', 'uyề': 'uiề', 'uyế': 'uiế', 'uyể': 'uiể', 'uyễ': 'uiễ', 'uyệ': 'uiệ'
}

break_word_character = ['space', 'enter', 'delete', '[', ']', '\\', ';', "'", ',', '.', '/', '`', '-', '=']
break_word_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
current_word = ''

def on_press_keyboard(event):
    global current_word
    if event.name in break_word_character or event.name in break_word_number:
        current_word = ''
    elif event.name == 'backspace':
        if len(current_word) > 0:
            current_word = current_word[:-1]
    
    if len(str(event.name)) == 1 and re.match("^[A-Za-z0-9_-]*$", event.name):
        current_word = current_word + str(event.name)
        print(current_word)

    if len(str(current_word)) > 0 and len(str(current_word)) < 7:
        search = unidecode.unidecode(current_word)
        
        if search.lower() in mapping_scheme:
            for x in range(len(search) + 1):
                keyboard.send('backspace')
            keyboard.write(str(mapping_scheme[search]))
    else:
        current_word = ''

keyboard.on_press(on_press_keyboard)

while True:
    pass