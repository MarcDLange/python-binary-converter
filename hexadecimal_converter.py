hexadecimal = []
number = 1622558


def calculate(number):
    result = divmod(number, 16)
    hexadecimal.append(result[1])
    if result[0] > 0:
        calculate(result[0])


if number < 16:
    print(number)
else:
    if number > 9:
        if number == 10:
            print('A')
        if number == 11:
            print('B')
        if number == 12:
            print('C')
        if number == 13:
            print('D')
        if number == 14:
            print('E')
        if number == 15:
            print('F')
        elif number > 15:
            calculate(number)
hexadecimal.reverse()
new_hex = []
for x in hexadecimal:
    if x == 10:
        new_hex.append('A')
    elif x == 11:
        new_hex.append('B')
    elif x == 12:
        new_hex.append('C')
    elif x == 13:
        new_hex.append('D')
    elif x == 14:
        new_hex.append('E')
    elif x == 15:
        new_hex.append('F')
    else:
        new_hex.append(x)

print(new_hex)
"""
temporary_string = ''
for value in new_hex:
    temporary_string = temporary_string + str(value)
new_hex = temporary_string
"""