from morse_code import GetMorseCode

morse_code = GetMorseCode().morse_code

def morser_code_converter():
    translation = ""
    text = input('Please put in a word, phrase or sentence to translate (english characters and numbers only):\n').upper().split()
    for word in text:
        for char in word:
                translation += morse_code[char]
                translation += '  '
        translation += ' /  '
    print(translation)

morser_code_converter()