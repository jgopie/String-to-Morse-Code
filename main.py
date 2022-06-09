import config
from playsound import playsound


def to_morse(english: str) -> str:
    english_list = [i.upper() for i in english]
    converted_string = ''
    for letters in english_list:
        if letters not in config.CODE:
            return 'A character is not represented in our morse code dictionary.'
        else:
            converted_string = converted_string + config.CODE[letters]
    return converted_string


def play_string(morse_code: str):
    morse_list = [i for i in morse_code]
    for character in morse_list:
        if character == '.':
            playsound('sounds/short_beep.mp3')
        elif character == '-':
            playsound('sounds/long_beep.mp3')
        else:
            return print('Something went terribly wrong.')


user_input = input('Please enter the string you wish to convert: ')
morse_string = to_morse(user_input)
print(morse_string)
user_input = input('Would you like to play this code?(y/n): ')

if user_input.lower() == 'y':
    play_string(morse_string)
else:
    print('See ya!')
