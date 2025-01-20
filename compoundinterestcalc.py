while True:
    try:
        initial = float(input("Enter Initial Amount: "))
    except ValueError:
        print("Please enter your initial amount of $")
        continue
    
    while True:
        try:
            percent = float(input("Enter your interest %: "))
            break
        except ValueError:
            print("Enter a your interest % (Do not use '%' symbol)")
            continue

    while True:
        try:
            monthly = input("Is your interest compounded monthly? (Y/N)")
            if monthly.lower() == 'y':
                break
            elif monthly.lower() == 'n':
                break
        except ValueError:
            print("Invalid Input. Specify using Y or N")
            continue

    while True:
        try:
            v = float(input("Enter amount of Months: "))
            break
        except:
            print("Enter a valid amount of months")
            continue
    if monthly.lower() == 'y':
        amount = initial * (1 + percent / 100 / 12) ** (12 * (v / 12))
        print(f"${round(amount, 2)}")
    elif monthly.lower() == 'n':
        print(f"${round(initial * ((1 + percent/100) ** (v / 12)), 2)}")

    while True:
        redo = input("Calculate again? (Y/N): ")
        if redo.lower() == 'n':
            print("Goodbye")
            exit()
        elif redo.lower() == 'y':
            break
        else:
            print("Invalid Input. Please enter Y or N")
            continue