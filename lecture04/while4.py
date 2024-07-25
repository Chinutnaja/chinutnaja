row = int(input("How many rows?: "))
colums = int(input("How many colums?: "))

i = 0

while i < row:
    j = 0
    while j < colums:
        print("*", end=" ")
        j += 1
    print()
    i += 1