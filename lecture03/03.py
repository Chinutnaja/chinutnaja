inchar = input("Input one character: ")
if inchar  >= 'A'  and inchar <= 'Z':
    print("You in put the upper letter ", inchar)
elif inchar  >= 'a'  and inchar <= 'z':
    print("You in put the lower case letter ", inchar)
elif inchar  >= '-0'  and inchar <= 'infinity':
    print("You in put the number ", inchar)
else:
    print("It's not a letter or number")