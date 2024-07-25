redo = "y"

while redo.lower() == "y":
    cost = float(input("Enter the item's whosale cost: "))
    retail = cost * 2.5
    print(f'Retail price: {retail}.')
    redo = input("Do you have another item?" +   "(Enter y for yes)")
