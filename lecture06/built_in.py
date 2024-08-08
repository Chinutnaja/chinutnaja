number = [4,2,9,1,5,6]

length = len(number)
print(f"Length of the list: {length}")

total_sum = sum(number)
print(f"Sum of all elements: {total_sum}")

max_value = max(number)
print(f"Maximum value: {max_value}")

min_value = min(number)
print(f"Minimum value: {min_value}")

sorted_number = sorted(number)
print(f"Sorted list: {sorted_number}")

bool_list = [False,True,False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_ture = all(bool_list)
print(f"Are all elements True? {all_ture}")

string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}")

reversed_numbers = list(reversed(number))
print(f"Reversed ist: {reversed_numbers}")

enumerated_numbers = list(enumerate(number))
print(f"Enumerated list: {enumerated_numbers}")