from math import *
print("Nhập vào số n")
a=int(input())
for i in range(1,a+1) :
    s=0
    b=i
    while (b>0) :
        s+=pow((b%10),3)
        b=b//10
    if i==s : print(i)
    print("Nhap n:")
