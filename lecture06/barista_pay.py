num = 6

def main():
    hours = [0] * num

    for index in range(num):
        print('Enter the hours worked by employee', \
               index + 1, ": ", sep=" ", end=" ")
        hours[index] = float(input())

    pay = float(input("Enter the hourly pay rate:"))
    
    for index in range(num):
        gross = hours[index] * pay
        print("Gross pay for employee", index + 1, ":$", \
              format(gross, ",.2f"), sep="")
    
main()
 