n=int(input("Nhập số n :"))
s=int(input("Nhập vào số đầu tiên :"))
a=[s,s]
for i in range(2,n+1):
	s=s*2
	a.append(s)
print(a)
