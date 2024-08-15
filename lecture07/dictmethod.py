phonebook = {"Anirach": "777-1111", "Micky": "777-2222", "Donald": "777-3333"}
heroesdict = {}
heroesdict["Hulk"] = "888-1111"
heroesdict["Iron man"] = "888-2222"
print(heroesdict.get("Hulk", "key not Found"))
print(heroesdict.get("Hulk", "key not Found"))

for key, value in phonebook.items():
    print(key,value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop("Mick", "Element not found"))
print(phonebook.pop("Micky", "Element not found"))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print("After clear")
print(phonebook)