def generate_prime(n):
    if n < 2:
        return ""
    prime = (2,3,5,7,11,13,17,19,23)
    if n in range(prime):
        print(n, end=" ")

print(generate_prime(10))
    


