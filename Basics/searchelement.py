a = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(a):
    num = int(input("Enter " + str(i) + "th number: "))
    arr.append(num)

print(arr)

num=int(input("Enter a number you want to check if its available or not : "))

if num in arr:
    print("Yes present")
else:
    print("Not present")
