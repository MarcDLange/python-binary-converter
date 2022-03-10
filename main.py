import sys
import util
import binaryconverter
import hexadecimal_converter

bc = binaryconverter
hx = hexadecimal_converter
number_list = []


def welcome():
    print('=====================================')
    print('|  Welcome to binary converter 1.2  |')
    print('|  Please enter a decimal number to |')
    print('|  convert it into a binary number. |')
    print('=====================================')


def mode_selection(user_input):
    global number_list
    if user_input == '1':
        print('Enter your decimal number: ')
        user_input = input()
        bc.convert(user_input, number_list)
        util.reverse_string_output(number_list)
    elif user_input == '2':
        print('Enter your decimal number: ')
        user_input = input()
        hx.convert(user_input, number_list)
        util.reverse_string_output(number_list)
    else:
        print('Invalid input!')
        mode_selection(input())
        


def instructions():
    print('Enter [1] to calculate a binary number')
    print('or [2] to calculate a hexadecimal number.')

"""
def validate_input():
    try:
        user_input = input()
        return int(user_input)
    except ValueError:
        print('Could not convert your input into a number')
        return 0
"""

def convert_again():
    print('Do you want to start over? [1] yes [2] no: ', end='')
    run_again = input()
    if run_again == '1':
        instructions()
        mode_selection(input())
    elif run_again == '2':
        print('Exiting...')
        sys.exit(0)
    else:
        print('Wrong input!')
        convert_again()


if __name__ == '__main__':
    welcome()
    instructions()
    print('Make a choice: ', end='')
    # user_input = validate_input()
    user_input = input()
    mode_selection(user_input)
    convert_again()
