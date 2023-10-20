import sys

if len(sys.argv) != 2:
    print("Missing command-ling argument")
    sys.exit(1) #echo $? to make sure that 1 displays
    
print(f"hello, {sys.argv[1]}")
sys.exit(0)