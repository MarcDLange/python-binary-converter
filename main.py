import sys
import Util
import BinaryConverter
import HexadecimalConverter

bc = BinaryConverter
hx = HexadecimalConverter
number_list = []


def welcome():
    print('=====================================')
    print('|  Welcome to binary converter 1.2  |')
    print('|  Please enter a decimal number to |')
    print('|  convert it into a binary number. |')
    print('=====================================')


def mode_selection(user_input):
    global number_list
    if user_input == 1:
        print('Enter your decimal number: ')
        user_input = input()
        bc.convert(user_input, number_list)
        Util.reverse_string_output(number_list)
    elif user_input == 2:
        print('Enter your decimal number: ')
        user_input = input()
        hx.convert(user_input, number_list)
        Util.reverse_string_output(number_list)
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


if __name__ == '__main__':
    welcome()
    instructions()
    print('Make a choice: ', end='')
    user_input = validate_input()
    mode_selection(user_input)
