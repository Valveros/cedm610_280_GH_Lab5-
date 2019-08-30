def add(first, second, call=2):
    if call != 2:
        result = first + second
        based = convert_base(result, first)
        return based
    return first + second
#
def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second)
        count -= 1
        if count == 0:
            return length
        else:
            return internal(second, third, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    #while current != 0:
    remainder = current % n
    if remainder > 9 and remainder < 16:
        remainder_string = HEX_CHARS[remainder]
    elif remainder >= 36:
        remainder_string = '('+str(remainder)+')'
    else:
        remainder_string = str(remainder)
    new_num_string = remainder_string+new_num_string
    current = current/n
    return new_num_string

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
    