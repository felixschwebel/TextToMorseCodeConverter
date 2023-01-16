from morse_code import GetMorseCode

morse_code = GetMorseCode().morse_code


def morse_code_converter():
    translation = ""
    text = input('Please put in a word, phrase or sentence to translate (english characters and numbers only):\n').upper().split()
    for word in text:
        for char in word:
            try:
                translation += morse_code[char]
                translation += '  '
            except KeyError:
                print('Please only use letters and numbers!')
                return morse_code_converter()
        translation += ' /  '
    print(translation)
    print('\n+++++++++++++++++++++++++++++++')
    cont = input('Do you want to translate something else? (y/n)\n')
    if cont == 'y':
        morse_code_converter()
    else:
        return False


print('🄼🄾🅁🅂🄴 🄲🄾🄳🄴 🅃🅁🄰🄽🅂🄻🄰🅃🄸🄾🄽')
while morse_code_converter():
    morse_code_converter()