# CAESAR CIPHER WITH KEY OPTION
# OldKalash7

import pyperclip


def main():
    userInput = int()

    print("CAESAR CIPHER\n----------------")
    print('SET MODE:')
    print('1. DECRYPT')
    print('2. ENCRYPT')
    userInput = int(input())

    if userInput == 1:
        print('wip')
    elif userInput == 2:
        encrypt()
    else:
        print('INVALID COMMAND, TRY AGAIN')
        main()


def encrypt():
    message = ""
    encrypted = ""
    key = 0
    counter = 0
    message = input('ENTER A MESSAGE TO ENCRYPT: ')
    key = int(input('SET KEY: '))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    for i in message:
        if i in alphabet:
            test = len(alphabet)
            counter = alphabet.find(i)
            if counter >= len(alphabet) - 1:
                counter -= len(alphabet)
            elif counter < 0:
                counter += len(alphabet)
            encrypted += alphabet[counter + key]
    print(encrypted)


if __name__ == '__main__':
    main()
