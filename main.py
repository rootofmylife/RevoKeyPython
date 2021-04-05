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
keyboard.add_abbreviation('ia', 'iê', match_suffix=True)
# VNI
keyboard.add_abbreviation('iaf', 'iề', match_suffix=True)
keyboard.add_abbreviation('ias', 'iế', match_suffix=True)
keyboard.add_abbreviation('iar', 'iể', match_suffix=True)
keyboard.add_abbreviation('iax', 'iễ', match_suffix=True)
keyboard.add_abbreviation('iaj', 'iệ', match_suffix=True)
# Telex
keyboard.add_abbreviation('ia2', 'iề', match_suffix=True)
keyboard.add_abbreviation('ia1', 'iế', match_suffix=True)
keyboard.add_abbreviation('ia3', 'iể', match_suffix=True)
keyboard.add_abbreviation('ia4', 'iễ', match_suffix=True)
keyboard.add_abbreviation('ia5', 'iệ', match_suffix=True)

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

while True:
    pass