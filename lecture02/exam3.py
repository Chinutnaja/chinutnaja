celsius = float(input("Enter temperature in celsius: "))
farenhiet = (celsius * 9/5) + 32
kelvin = (celsius + 273.15)

print("Tempreature in Fahrenheit is: ", format(farenhiet, '.2f'))
print("Tempreature in kelvin", format(kelvin, '.2f'))