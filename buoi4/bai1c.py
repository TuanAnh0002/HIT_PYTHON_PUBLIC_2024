n=int(input("Nhập số n :"))
a=[]
for i in range(0,n):
	a.append(int(input("Nhập vào :")))
b=int(input("Nhập số Y:"))
a.insert(0,b)
print(a)
c=sorted(a)
d=sorted(a,reverse=True)
if(a==c):
	print("Tăng")
elif(a==d):
	print("Giam")
else:
	print("NO")
