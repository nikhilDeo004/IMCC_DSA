a = int(input("Enter the number "))

# for i in range((a*2)+1):
#     if(i== a+1):
#         print("*"*((a*2)+1))
#     else:
#         print(" "*a+"*")

for i in range(a):
    for j in range(a):
        if(j==a//2 or i==a//2):
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()


    
