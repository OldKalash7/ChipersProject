# CAESAR CIPHER WITH KEY OPTION
# OldKalash7

import pyperclip


def main():

    mode_decrypt = False  # Sets the mode, false for decrypt
    user_input = int()

    try:
        print("CAESAR CIPHER\n-------------")
        print('SET MODE:')
        print('1. DECRYPT')
        print('2. ENCRYPT')

        user_input = int(input())

        if user_input == 1:
            mode_decrypt = True
            cipher(mode_decrypt)
        elif user_input == 2:
            cipher(mode_decrypt)
        else:
            print('INVALID COMMAND, TRY AGAIN')
            main()

    except ValueError:
        print("ERROR, MODE SET TO ENCRYPT")
        cipher(mode_decrypt)


def cipher(mode):

    LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    message = ''  # Stores the message to encrypt
    encrypted = ''  # Stores the encrypted or decrypted message
    key = 0

    message = input('ENTER A MESSAGE: ')
    message = message.upper()

    try:
        key = int(input('SET KEY: '))
    except ValueError:
        key = 1
        print("DEFAULT KEY: 1")
    except IndexError:
        key = 1
        print("DEFAULT KEY: 1")

    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            if mode is False:
                num = num + key
            elif mode is True:
                num = num - key
            # Wrap if the set of letters it's not enough
            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            encrypted += LETTERS[num]
        else:
            encrypted += letter

    print(encrypted)
    pyperclip.copy(encrypted)


if __name__ == '__main__':
    main()
