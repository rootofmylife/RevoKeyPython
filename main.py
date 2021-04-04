import re
import keyboard

from tkinter import *

mapping_consonant_type_one = {
    'q': 'k',
    'd': 'z',
    'r': 'z',
    'x': 's',
}

mapping_consonant_type_two = {
    'tr': 'c',
    'gi': 'z',
    'nh': 'ń',
    'ph': 'f',
    'kh': 'x',
    'th': 'q',
}

mapping_consonant_type_three = {
    'c': 'k',
    'ch': 'c',
    'ng': 'w',
    'ngh': 'w',
}

mapping_vowel = {
    'ia': 'iê', 'ìa': 'iề', 'ía': 'iế', 'ỉa': 'iể', 'ĩa': 'iễ', 'ịa': 'iệ',
    'uan': 'ua', 'uản': 'ủa', 'uàn': 'ùa', 'uán': 'úa', 'uãn': 'ũa', 'uạn': 'ụa',
    'uang': 'ua', 'uàng': 'ùa', 'uáng': 'úa', 'uảng': 'ủa', 'uãng': 'ũa', 'uạng': 'ụa',
    'uai': 'ua', 'uài': 'ùa', 'uái': 'úa', 'uại': 'ụa', 'uải': 'ủa', 'uãi': 'ũa',
    'uay': 'ua', 'uày': 'ùa', 'uáy': 'úa', 'uạy': 'ụa', 'uảy': 'ủa', 'uãy': 'ũa',
    'ua': 'uô', 'uôs': 'uố', 'uôf': 'uồ', 'uôr': 'uổ', 'uôx': 'uỗ', 'uôj': 'uộ', # end of morpho
    'uô1': 'uố', 'uô2': 'uồ', 'uô3': 'uổ', 'uô4': 'uỗ', 'uô5': 'uộ',
    'uyee': 'uiê', 'uiêf': 'uiề', 'uiês': 'uiế', 'uiêr': 'uiể', 'uiêx': 'uiễ', 'uiêj': 'uiệ', # Telex: uyê - > uiê
    'uye6': 'uiê', 'uiê2': 'uiề', 'uiê1': 'uiế', 'uiê3': 'uiể', 'uiê4': 'uiễ', 'uiê5': 'uiệ' # Telex: uyê - > uiê
}

current_word = ''

def on_press_keyboard(event):
    global current_word

    if (str(event.name).isalpha() or str(event.name).isdigit()) and len(str(event.name)) == 1:
        if len(current_word) > 5:
            current_word = ''
        else:
            current_word = current_word + str(event.name)

        if current_word in mapping_consonant_type_one:
            # keyboard.send('backspace') # remove last character
            # keyboard.write(str(mapping_consonant_type_one[current_word]))
            current_word = ''
        elif current_word in mapping_consonant_type_two:
            keyboard.send('backspace') # remove last character
            keyboard.send('backspace') # remove second last character
            keyboard.write(str(mapping_consonant_type_two[current_word]))
            current_word = ''
        elif current_word in mapping_consonant_type_three:
            keyboard.write(str(mapping_consonant_type_three[current_word]))
            current_word = ''
    else:
        current_word = ''

keyboard.on_press(on_press_keyboard)
keyboard.remap_key('q', 'k')
keyboard.remap_key('d', 'z')
keyboard.remap_key('r', 'z')
keyboard.remap_key('x', 's')

while True:
    pass