
import unidecode
import keyboard

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

def on_press_keyboard(event):
    if event.name == 'space' or event.name == '.' or event.name == ',' or event.name == ';' or event.name == 'enter':
        print("goooo")

keyboard.on_press(on_press_keyboard)

while True:
    pass