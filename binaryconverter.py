def convert(decimal, result_list):
    result = divmod(decimal, 2)
    result_list.append(result[1])
    if result[0] > 0:
        convert(result[0], result_list)

"""
binary = []
convert(5,binary)
"""
binary = []
convert(5,binary)