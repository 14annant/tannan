for i in range(3):
    print("#" *3)
    


'''
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()

###
for i in range(4):
    print("?", end="")
print()

print("?" *5)
####
def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n= int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


main ()
'''