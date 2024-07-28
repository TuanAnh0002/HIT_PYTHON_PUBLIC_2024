n=int(input("Nhập số n :"))
a=[]
for i in range(0,n):
	a.append(input("Nhập vào :"))
b=input("Nhập số X:")
c=0
for i in range(0,n):
	if(b==a[i]):
		c=c+1

print("Số lần X xuất hiện trong list là :",c)

