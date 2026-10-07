a = int(input("Enter the number of elements in the array: "))
arr = []

for i in range(a):
    num = int(input("Enter " + str(i) + "th number: "))
    arr.append(num)

print(arr)

largest = max(arr)
smallest = min(arr)

s=sorted(arr)

second_largest=s[3]
second_smallest=s[-1]


print("Largest:", largest)
print("Second largest:", second_largest)
print("Smallest:", smallest)
print("Second smallest:", second_smallest)