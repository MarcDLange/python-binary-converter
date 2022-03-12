def reverse_string_output(string):
    string.reverse()
    temporary_string = ""
    for value in string:
        temporary_string = temporary_string + str(value)
    string = temporary_string
    print(string)