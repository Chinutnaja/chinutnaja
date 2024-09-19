filename = input("Enter the name of the file: ")
try:
    infile = open(filename, "r")
    content = infile.read()
    print(content)
    infile.close()

except FileNotFoundError as e:
    print(f"Eror: {e}")

print("End of program")