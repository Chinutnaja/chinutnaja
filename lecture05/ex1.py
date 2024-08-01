def is_armstrong(numbers):
    str_num = str(numbers)
    num_digits = len(str_num)
    total = 0

    for digit in str_num:
        total = total + int(digit) ** num_digits
        if total == numbers:
            return True
        else:
            return False

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))