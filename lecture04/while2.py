keep_doing = "y"

while keep_doing.lower() == "y":
    sales = float(input("Enter the amout of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    commission = sales * comm_rate
    print(f'THe commision is ${commission:.2f}')
    keep_doing = input("DO you want to calculate another" + \
                   "commission (Enter y for yes):" )