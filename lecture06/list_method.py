heroes = ["Ironman", "Thor", "Hulk", "Superman", "spiderman"]
h2 = ["Dr.strange", "Cpt. America", "Black panther", "Ant man"]

heroes.insert(0, h2[0])
print(heroes.index("Thor"))
heroes.insert(heroes.index("Thor"), h2[1])
print(heroes)
heroes.remove("Superman")
heroes.append("Ant man")
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] = "Wonder women"
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = "Human"
print(heroes)
print(copyheroes)