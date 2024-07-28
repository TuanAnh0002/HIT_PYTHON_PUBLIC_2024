a=[]
k=int(input("Nhập số phần tử k :"))
for i in range(0,k):
	a.append(int(input(f'a[{i}]=')))
n=int(input("Nhập số cột :"))
m=int(input("Nhập số dòng :"))

if(n * m > k):
	print(NO)
else :
	b = [[0]*m for i in range(n)]
	c=0
	for i in range(n):
		for j in range(m):
			if c < len(a):
				b[i][j]=a[c]
				c+=1

print(b)