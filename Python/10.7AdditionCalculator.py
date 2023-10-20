#adds 2 numbers if one of the values is not a number the test does not pass

print("Enter 2 numbers and I will add them\n")

while True:
    num1 = input("First Number: \n")
    num2 = input("Second Number: \n")

    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("One of the values is not allowed")
    else:
        print(f"\n{num1} + {num2} = {answer}")
        break