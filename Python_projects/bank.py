user_input = input("Greeting: ")
greeting = user_input.lower()

if greeting == "hello" or greeting[0:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
