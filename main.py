import re
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

def place_word(found_word, trigger):
    for x in range(len(found_word) + 1):
        keyboard.send('backspace')
    keyboard.write(found_word)

def db_search_to_list(search_term):
    global found_words
    if search_term.lower() in mapping_scheme:
        found_words.append(str(mapping_scheme[search_term]))

    if len(found_words) > 1:
        print(found_words)

def on_press_keyboard(event):
    global words, found_words, equal_sign_press_counter
    if event.name == 'space' or event.name == '.' or event.name == ',' or event.name == ';' or event.name == 'enter':
        words = ''
    elif event.name == 'backspace':
        if len(words) > 0:
            words = words[:-1]
    elif event.name == 'delete':
        found_words = []
    elif event.name == '=':
        if len(str(words)) > 0:
            search = unidecode.unidecode(words)
            found_words = [search]
            equal_sign_press_counter = 1
            db_search_to_list(search)
        words = ''
        if len(found_words) > 1:
            print(str(equal_sign_press_counter) + " - " + found_words[equal_sign_press_counter])
            place_word(str(found_words[equal_sign_press_counter]), str(event.name))
            equal_sign_press_counter = equal_sign_press_counter + 1
            if equal_sign_press_counter > len(found_words) - 1:
                equal_sign_press_counter = 0
    else:
        # print(event.name)
        if len(str(event.name)) == 1:
            if re.match("^[A-Za-z0-9_-]*$", event.name):
                words = words + str(event.name)

keyboard.on_press(on_press_keyboard)

while True:
    pass