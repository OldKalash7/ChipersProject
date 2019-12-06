# This cipher takes a string and encrypts it turning it around

import pyperclip


def main():
    message = ''
    print('ENTER A STRING TO ENCRYPT: ')
    message = str(input())
    print('THIS IS YOUR MESSAGE ENCRYPTED, COPIED TO CLIPBOARD')
    print(reversecipher(message))


def reversecipher(message):
    encrypted = ''
    i = len(message) - 1
    while i >= 0:
        encrypted += message[i]
        i -= 1
    pyperclip.copy(encrypted)
    return encrypted


if __name__ == '__main__':
    main()
