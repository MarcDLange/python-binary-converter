def convert(decimal, conversion_result):
    calculation_result = divmod(int(decimal), 2)
    conversion_result.append(calculation_result[1])
    if calculation_result[0] > 0:
        convert(calculation_result[0], conversion_result)
    return conversion_result
