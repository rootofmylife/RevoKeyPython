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
    'ch': 'c', # ch -> c
    'tr': 'c',
    'ng': 'w',
    'wh': 'w', # ngh -> w
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
current_word = ''

def on_press_keyboard(event):
    global current_word, waiting_scheme_flag
    if event.name in break_word_character:
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
            for x in range(len(search)):
                keyboard.send('backspace')
            keyboard.write(str(mapping_scheme[search]))
            current_word = str(mapping_scheme[search])

keyboard.on_press(on_press_keyboard)

while True:
    pass