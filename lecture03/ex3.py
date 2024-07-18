hour = float(input("please enter ur Hours"))
pay =  float(input("pls enter ur payrate"))
if hour > 40:
    print("Your gross pay is", ((40 * pay) + ((hour - 40 ) * 1.5 * pay)))
else: 
    print("Your gross is ", hour * pay)