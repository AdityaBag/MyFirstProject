x = float(input("Enter number to check if its greater than 3"))
y = float(input("Enter number to check if it even or not"))
if x > 3 and y % 2 == 0:
    print("Both of the condions are satisfied")
elif x > 3 or y % 2 == 0:
    if x > 3 and y % 2 != 0:
        print("First condition is satisfied")
    else:
        print("Second condtion is satisfied")
else:
    print("None of the conditions are satisfied")
