columns = int(input("How many columns>"))
number = 1
while number <= 100:
    colum = 0
    while colum < columns and number <= 100:
        print(f"{number}", end=" ")
        number += 1
        colum += 1
    print()