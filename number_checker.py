import math
while True:
    # Check if value is a valid number
    try:
        number = float(input("Enter Number: "))
    except ValueError:
        print("This is a number checker, use a number")
        continue
    # Few numbers we dont wanna calculate
    if number == 0:
        print("ZA ZERO!!!!!!!!")
    elif number < 0:
        print("Idk how to make it so that roots dont happen for negative numbers, sorry. Perhaps you might know how?")
        continue
    else:
        print(f"The number {number} is:")
        # Check if a number is even/odd
        if number / 2 == int(number / 2):
            print("Even")
        else:
            print("Odd")
        # Check if a number is a Perfect Square (accounting for floating point error)
        if round(math.sqrt(number)) == int(round(math.sqrt(number))):
        # Could be rewritten as if number ** (1 / 2) == int(number ** (1 / 2))
            print("Perfect Square")
        else:
            print("Not a Perfect Square")
        # Check if a number is a perfect cube (accounting for floating point errors)
        if round(number ** (1 / 3)) == int(round(number ** (1 / 3))):
            print("Perfect Cube")
        else:
            print("Not a Perfect Cube")
    continue