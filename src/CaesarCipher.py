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

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    encrypted = ""
    key = 0  # Added or subtracted to counter, to form the encrypted message.
    counter = 0  # Stores the position of the letter in the alphabet

    message = input('ENTER A MESSAGE TO ENCRYPT: ')
    message = message.upper()

    try:
        key = int(input('SET KEY: '))
    except ValueError:
        key = 1
        print("DEFAULT KEY: 1")

    for letter in message:
        if letter in alphabet:
            counter = alphabet.find(letter)
            # Wrap if the set of letters it's not enough
            if counter >= len(alphabet) - 1:
                counter -= len(alphabet)
            elif counter < 0:
                counter += len(alphabet)
            # Encrypt or Decrypt the message
            if mode is False:
                encrypted += alphabet[counter + key]
            elif mode is True:
                encrypted += alphabet[counter - key]

    print("MESSAGE COPIED TO CLIPBOARD")
    print(encrypted)
    pyperclip.copy(encrypted)  # Copies the message to the clipboard


if __name__ == '__main__':
    main()
