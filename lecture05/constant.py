import random 

heads = 1
tails = 2
tosses = 10

def toses_coin():
    for toss in range(tosses):
        if random.randint(heads,tails) == heads:
            print("Heads")
        else:
            print("Tails")

toses_coin()