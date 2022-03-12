decimal = int(input())
binary_number = []

def calculate(number):
    if(number % 2 != 0):
        binary_number.append(1)
    else:
        binary_number.append(0)
    result = divmod(number, 2)
    whole_number = result[0]
    return whole_number

while(decimal >= 1):
    decimal = calculate(decimal)

binary_number.reverse()
temporary_string = ""

for value in binary_number:
    temporary_string = temporary_string + str(value)
binary_number = temporary_string

print(binary_number)