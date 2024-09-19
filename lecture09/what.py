y = int(input("Enter a number: "))
try:
    x = 1 / y 
except ZeroDivisionError as e:
    print("you cannot divided by zero")
print(x)



print("End of program")