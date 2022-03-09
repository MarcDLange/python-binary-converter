binary_number = []

def welcome():
    print('=====================================')
    print('|  Welcome to binary converter 1.1  |')
    print('|  Please enter a decimal number to |')
    print('|  convert it into a binary number. |')
    print('=====================================')


def instructions():
    print('\nEnter a decimal number: ', end='')


def get_input_as_int():
    try:
        user_input = input()
        return int(user_input)
    except ValueError:
        print('Could not convert your input into a number')
        return 0


def convert_into_binary(decimal):
    global binary_number
    result = divmod(decimal, 2)
    binary_number.append(result[1])
    if result[0] > 0:
        convert_into_binary(result[0])
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
    user_input = get_input_as_int()
    convert_into_binary(user_input)
