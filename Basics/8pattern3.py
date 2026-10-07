n=int(input("Enter a number :"))

arr1=[]
arr2=[]
for i in range(n-1,-1,-1):
    arr1.append(i)

print(arr1)

print()

for i in range(-1,n+3,+2):
    arr2.append(i)

arr2[0]=0
print(arr2)

for i in range(n):
    if(i==0):
        print(" "*(arr1[i]) + "*")
    else:
        print(" "*(arr1[i]) + "*" + " "*arr2[i] + "*")


for i in range(n-2, -1, -1):
    if(i==0):
        print(" "*(arr1[i]) + "*")
    else:
        print(" "*(arr1[i]) + "*" + " "*arr2[i] + "*")