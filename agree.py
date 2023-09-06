s = input("Do you agree?")

#if s =="Y" or s =="y":
s= s.lower()
if s in ['y','yes']:
    print("Agreed.")
elif s in ['n','no']:
    print("Not agreed.")
