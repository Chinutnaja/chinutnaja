score = float(input("Enter ur first score: "))
score2 = float(input("Enter ur second score: "))
score3 = float(input("Enter ur 3rd score: "))
AvG =  (score + score2 + score3) / 3

print(AvG)

if AvG > 95:
    print("Congratulations!!")
else:
    print("Your fail")
