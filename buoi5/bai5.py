a=int(input("nhập số n :"))
b=[]
c=[]
for i in range (n) :
	b.append(int(input("Nhập vào danh sách 1 :")))
	c.append(int(input("Nhập vào danh sách 2:")))

for i in range(n):
	if(c[i]>0):
		print("Nhập lại :")
		c.append(int(input("Nhập vào danh sách 2:")))

