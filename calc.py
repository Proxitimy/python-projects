#adds numbers
def add(a, b):
    return a + b

#subtracts numbers
def sub(a, b):
    return a - b

#multiplies numbers
def mul(a, b):
    return a * b

#divides numbers
def div(a, b):
    return a / b

print("What u wanna dos?")
print("1. Addition")
print("2. Subtraction?")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1, 2, 3, 4): ")
    if choice in ['1', '2', '3', '4']:
        while True:
            try:
                digit1 = float(input("Put in the first number: "))
                digit2 = float(input("Enter second number: "))
                break
            except ValueError:
            # Invalid number handler
                print("Invalid input. Please enter a number.")
                continue
    else:
        # Invalid choice handler
        print("Invalid input. Please enter a valid choice (1, 2, 3, 4).")
        continue

    if choice == '1':
        print(digit1 + digit2)
    if choice == '2':
        print(digit1 - digit2)
    if choice == '3':
        print(digit1 * digit2)
    if choice == '4':
        print(digit1 / digit2)
        
    while True:
        redocalc = input("Another calc? (Y/N): ")
        # lower() is there so you can type either lowercase or uppercase input (i feel very smart for figuring this out)
        if redocalc.lower() == 'n':
          print("Goodbye mr")
          exit()
        elif redocalc.lower() == 'y':
           break
        else:
           print("Invalid input. Please enter Y or N.")