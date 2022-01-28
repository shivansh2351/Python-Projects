weight = int(input("weight: "))
unit = input("Kg or Lbs: ")

if unit.upper() == "K":
    converted = weight * 2.204
    print("weight in Lbs: ", str(converted))
elif unit.upper() == "L":
    converted = weight / 2.204
    print("weight in kg: ", str(converted))
else:
    print("Enter right unit")
