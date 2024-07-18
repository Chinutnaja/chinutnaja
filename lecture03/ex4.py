print("""Please select operation
        1. add 
        2. subtract 
        3. multipy 
        4. divide
      """)
opt = float(input("pls select operation form: "))
first_num = float(input("pls type ur first number"))
second_num = float(input("pls type ur second number"))


if opt == 1:
    print(first_num + second_num)
elif opt == 2:
    print(first_num - second_num)
elif opt == 3:
    print(first_num * second_num)
elif opt == 4:
    print(first_num / second_num)
else:
    print("not have this choice")