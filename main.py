import sys
import marc_util as mcu
import binary_converter as bc
import hexadecimal_converter as hxc

conversion_result = []

def welcome():
    print('=====================================')
    print('|  Welcome to binary converter 1.2  |')
    print('|  Please enter a decimal number to |')
    print('|  convert it into a binary number. |')
    print('=====================================')


def mode_selection(user_input):
    global conversion_result
    if user_input == '1':
        print('Enter your decimal number: ')
        user_input = input()
        bc.convert(user_input, conversion_result)
        mcu.reverse_string_output(conversion_result)
    elif user_input == '2':
        print('Enter your decimal number: ')
        user_input = input()
        hxc.convert(user_input, conversion_result)
        mcu.reverse_string_output(conversion_result)
    else:
        print('Invalid input!')
        mode_selection(input())


def instructions():
    print('Enter [1] to calculate a binary number')
    print('or [2] to calculate a hexadecimal number.')


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
