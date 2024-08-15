phoneback = {"Anirach": "777-1111", "Micky": "777-2222", "Donald": "777-3333"}

phoneback["bart"] = [1,3,5]

elements = len(phoneback)
print("There are", elements, "names in phonebook")
for key in phoneback:
    print(key, "phone number is: ", phoneback[key])

phoneback["bart"][1] = 9
print(phoneback)