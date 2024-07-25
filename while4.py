row = int(input("How many rows?: "))
colums = int(input("How many colums?: "))

i = 0

for i in range(row):
    j = 0
    for j in range(colums):
        print("*", end="")
        j += 1
    print()
    j += 1
