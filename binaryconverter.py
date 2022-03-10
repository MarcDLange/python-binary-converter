def convert(decimal, result_list):
    result = divmod(int(decimal), 2)
    result_list.append(result[1])
    if result[0] > 0:
        convert(result[0], result_list)
    return result_list

binary = []
convert(5,binary)