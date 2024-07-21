print("Nhap n:")
n = int(input())
print("=======")
for i in range(1,n+1) :
    S=0
    for j in range(1,i) :
        if (i % j == 0) : 
            S+=j
    if i==S :
        print(i,end=" ")
