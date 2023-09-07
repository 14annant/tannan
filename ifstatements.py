'''
#5.8 hello admin and 5.9 no users

usernames = ["john", "tom", "admin", "george", "chris"]

if usernames == []:
    print("We need to find some users!")
for username in usernames:
    if username == "admin":
        print("hello admin would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")

# 5.11 ordinal Numbers

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else
        print(f"{number}st")
'''

 ##5.10 checking usernames   
    
current_users = ["john", "tom", "Jess", "George", "chris"]
new_users = ["alex", "kelly", "jess", "george", "ken"]

current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} you will have to enter a new username")
    else:
        print(f"User name {new_user} is availble")