# we'll verify if a number is within a certain range

def range_check(a):
    if a in range(10, 39):
        print(a, "is in range")
    else:
        print("The number isn't in range")

# checking if certain numbers are in range
range_check(50)
range_check(11)
range_check(23)
range_check(112)
range_check(26)
range_check(9)
