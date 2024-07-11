boys = int(input("How many boy in ur classroom: "))
girls = int(input("How many girls in ur classroom: "))
boyper = (boys  * 100) / (girls + boys)
girlper = (girls * 100) / (boys + girls)

print(f"You had  {boyper} percent boy in your classroom")
print(f"You had {girlper} percent girls in your classroom")