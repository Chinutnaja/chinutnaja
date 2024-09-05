with open("ex1.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()