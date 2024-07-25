max = 5
total = 0.0
print("this program calculates the sum of ")
print(max,"number you will enter.")

for x in range(max):
    number = int(input("Enter a number: "))
    total = total + number 

print("The total is", total)