a = int(input("Enter the number "))
for i in range(a):
    print("* ",end="")

print()

for i in range(a-2):
    print("*" + " "*(2*a-3) + "*")

for i in range(a):
    print("* ",end="")