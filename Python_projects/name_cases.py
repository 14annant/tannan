##this program is meant to do some string manipulations.
## lstrip(), rstrip() and strip() functions as well as upper(), lower(), and title() functions were used.

author = "Malcom Gladwell "
quote = " it takes 10,000 hours of intensive practice to achieve mastery of comples skills "
print(f'{author} once said "{quote}"')

message = author.rstrip() + ' "' + quote.strip() + '"'
print(message)



name = input("whats your name: ")
print(f"hello, {name.upper()} would you like to write some Python today?")

string = input("Write a string to see it manipulated.: ")
upper_string = string.upper()
lower_string = string.lower()
title_string = string.title()

print(f"Resuts:\n\tInput: {string}\n\t{upper_string}\n\t{lower_string}\n\t{title_string}")


