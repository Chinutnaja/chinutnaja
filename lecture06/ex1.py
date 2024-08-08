heroes = ["Ironman", "Thor", "Hulk", "Spiderman"]

def display():
    print(heroes)

def add():
    global heroes
    heroesadd = input("Pls input new heroes:")
    heroes.append(heroesadd)
    print(heroes)

def insert():
    global heroes
    heroesinsert = int(input("Pls input any number: "))
    heroes.insert(heroesinsert)
    print()

display()
add()
insert()