from morse_code import GetMorseCode

morse_code = GetMorseCode().morse_code


def morser_code_converter():
    translation = ""
    text = input('Please put in a word, phrase or sentence to translate (english characters and numbers only):\n').upper().split()
    for word in text:
        for char in word:
            try:
                translation += morse_code[char]
                translation += '  '
            except KeyError:
                return print('Please only use letters and numbers!')
        translation += ' /  '
    print(translation)
    print('\n+++++++++++++++++++++++++++++++')
    cont = input('Do you want to translate something else? (y/n)\n')
    if cont == 'y':
        morser_code_converter()
    else:
        return False

print('🄼🄾🅁🅂🄴 🄲🄾🄳🄴 🅃🅁🄰🄽🅂🄻🄰🅃🄸🄾🄽')
while morser_code_converter():
    morser_code_converter()