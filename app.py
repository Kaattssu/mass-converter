weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    calc1 = float(weight) * 2.20462
    print("Your weight is: " + str(calc1) + "lbs")
elif unit.upper() == "L":
    calc2 = float(weight) / 2.205
    print("Your weight is: " + str(calc2) + "kg")