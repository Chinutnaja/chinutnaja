row = 101
colums = int(input("How many colums?: "))

i = 0

while i < row:
    j = 0
    while j < colums + 1:
        print(" ", end="")
        j += 1
    print(i,end="")
    i += 1