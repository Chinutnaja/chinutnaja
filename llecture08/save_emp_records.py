num_emps = 3
with open("ex1.txt", "w")as emp_file:
    for count in range(1, num_emps + 1):
        print("Enter data for employee")
        name = input("Name: ")
        id_num = input("ID : ")
        dept = input("Dept: ")
        emp_file.write(f"Name: {name}" + "\n")
        emp_file.write(f"ID: {id_num}" + "\n")
        emp_file.write(f"Dept: {dept}")
        print()

print("Employee records written to ex1.txt")
