try:
    y = int(input("Enter a number: "))
    x = 1 / y 
except ZeroDivisionError as e:
    print("you cannot divided by zero")
except ValueError as e:
    print(f"Eror: {e}")



print("End of program")