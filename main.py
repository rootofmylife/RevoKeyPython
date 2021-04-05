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

def vowel_ia(event):
    if event.word == 'ìa':
        keyboard.send('backspace')
        keyboard.write('ê')

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

keyboard.add_abbreviation('ia', 'iê', match_suffix=True)
keyboard.add_word_listener('ìa', vowel_ia, match_suffix=True)
# keyboard.add_abbreviation('ía', 'iế', match_suffix=True)
# keyboard.add_abbreviation('ỉa', 'iể', match_suffix=True)
# keyboard.add_abbreviation('ĩa', 'iễ', match_suffix=True)
# keyboard.add_abbreviation('ịa', 'iệ', match_suffix=True)

while True:
    pass