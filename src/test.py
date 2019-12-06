# COMMENT
# HERE I TEST DIFFERENT PYTHON FUNCTIONS AND STATEMENTS, SO THIS DOES NOT MAKE ANY SENSE AT ALL

def main():
    a = 0
    b = 0
    print('Enter a value for A: ')
    a = int(input())
    print('Enter a value for B: ')
    b = int(input())
    print(add(a, b))
    forTest = 'hola'
    test = ''
    leng = len(forTest)
    for i in forTest:
        test += forTest[leng]
        leng = leng - 1


def add(first, second):
    return first + second


if __name__ == '__main__':
    main()
