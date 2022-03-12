import sys

binary_number = []
base = 0


def welcome():
    print('=====================================')
    print('|  Welcome to binary converter 1.2  |')
    print('|  Please enter a decimal number to |')
    print('|  convert it into a binary number. |')
    print('=====================================')


def mode_selection(user_input):
    global base
    if user_input == 1:
        base = 2
    elif user_input == 2:
        base = 16
    else:
        print('Invalid input!')
        sys.exit(0)
        


def instructions():
    print('Enter [1] to calculate a binary number')
    print('or [2] to calculate a hexadecimal number.')


def validate_input():
    try:
        user_input = input()
        return int(user_input)
    except ValueError:
        print('Could not convert your input into a number')
        return 0


def convert(decimal):
    global binary_number
    result = divmod(decimal, base)
    if base == 2:
        binary_number.append(result[1])
    elif result[0] > 9:
        print(result)
        binary_number.append('A')
    if result[0] > 0:
        convert(result[0])
    else:
        binary_number.reverse()
        temporary_string = ''
        for value in binary_number:
            temporary_string = temporary_string + str(value)
        binary_number = temporary_string
        print('Your decimal number in binary: ' + binary_number)


if __name__ == '__main__':
    welcome()
    instructions()
    print('Make a choice: ', end='')
    user_input = validate_input()
    mode_selection(user_input)
    print('\nEnter a decimal number: ', end='')
    user_input = validate_input()
    convert(user_input)
