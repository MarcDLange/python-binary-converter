# Cast the user 'input()' type as 'int()' values and assign
# them to the variable named 'decimal'.
decimal = int(input())

# Assign an empty list to the variable named 'binary_number'.
binary_number = []

# Define a new function called 'calculate()' with a parameter 
# named 'number'.
def calculate(number):
    # '%' is an operator called 'modulo'. It is used to divide numbers
    # with remainder.
    # If 'number' divided by 2 is not 0: (In other words: If the result
    # does not have a remainder.)
    if(number % 2 != 0):
        # Append a '1' to the end of the list that is assigned to
        # 'binary_number'.
        binary_number.append(1)
    else:
        binary_number.append(0)
    # 'divmod' is a function that returns a 'tuple' of the whole number
    # and the remainder of a division calculation.
    result = divmod(number, 2)
    # Get the value at index '0' of the tuple 'result' and assign it
    # to the variable called 'whole_number'.
    whole_number = result[0]
    # The 'return' keyword is used to exit a function and return
    # a value. 
    # Return the variable 'whole_number'.
    return whole_number

# The 'while' keyword is used to create a loop that runs until its
# condition is true.
# WARNING: You can accidentially create endless loops with while that
# can crash slow hardware.
# 'while' 'decimal' is bigger or equal to '1':
while(decimal >= 1):
    decimal = calculate(decimal)

# 'reverse()' the content of the list.
binary_number.reverse()

# Assing an empty string to the variable called 'temporary_string'.
temporary_string = ""

# In Python the 'for' keyword creates a loop that iterates through
# every value in a collection.
for value in binary_number:
    temporary_string = temporary_string + str(value)
binary_number = temporary_string

# 'print()' 'binary_number' to the display.
print(binary_number)