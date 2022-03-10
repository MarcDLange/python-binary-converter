def convert_to_letter(number):
    if number == 10:
       number = 'A'
    if number == 11:
        number = 'B'
    if number == 12:
        number = 'C'
    if number == 13:
        number = 'D'
    if number == 14:
        number = 'E'
    if number == 15:
        number = 'F'
    return number


def convert(decimal, result_list):
    result = divmod(int(decimal), 16)
    if result[1] > 9 and result[1] < 16:
        letter = convert_to_letter(result[1])
        result_list.append(letter)
    else:
        result_list.append(result[1])
    if result[0] > 0:
        convert(result[0], result_list)
    return result_list