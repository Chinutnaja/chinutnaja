phoneback = {"Anirach": "777-1111", "Micky": "777-2222", "Donald": "777-3333"}
print(phoneback)

print(phoneback["Micky"])
print(phoneback.get("Donald"))

key = "Pluto"
if key in phoneback:
    print(phoneback["pluto"])
else:
    print(key + 'not in phoneback')

phoneback["Simpson"] = "777-4567"
phoneback["Pluto"] = "777-4444"
phoneback["Micky"] = "777-2122"
print(phoneback)

del phoneback["Simpson"]
print(phoneback)