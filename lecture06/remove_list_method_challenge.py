fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi", "apple", "strawberry"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"FRuits after remove: {fruits_with_duplicates}")