# CAESAR CIPHER HACKING USING BRUTE FORCE
# OldKalash7


def main():
    decrypt()


def decrypt():

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = ''
    decrypted = ''

    message = input('ENTER THE MESSAGE TO DECRYPT: ')
    message = message.upper()

    for i in range(len(LETTERS)):
        decrypted = ''
        for letter in message:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                num -= i
                if num < 0:
                    num += len(LETTERS)
                decrypted += LETTERS[num]

            else:
                decrypted += letter
        print('Key %s: %s' % (i, decrypted))


if __name__ == '__main__':
    main()
