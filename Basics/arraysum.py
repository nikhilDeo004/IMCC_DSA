a = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(a):
    num = int(input("Enter " + str(i) + "th number: "))
    arr.append(num)

print(arr)

total = 0
for i in range(a):
    total += arr[i]

print(total)