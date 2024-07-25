input_string = int(input("Enter a sting: "))
modified_string = ""
vowels = "aeiouAEIOU"

for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_string += "1"
    else:
        modified_string += upper_char

print("modified sting:", modified_string)