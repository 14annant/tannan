import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("NAMe: ")


if name in names:
    print("found")
    sys.exit(0)

print("Not found")
sys.exit(1)


'''
#this is a linear search
for n in names:
    if name == n:
        print("found")
        sys.exit(0)

'''