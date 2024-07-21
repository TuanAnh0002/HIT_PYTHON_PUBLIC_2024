print("Hãy nhập vào một số :")
a=int(input())
while (a<=0):
	print("Nhập lại giá trị :")
	a = int(input())

b=0
for i in range(1,10):
	if a % i == 0 :
		b = b + i 

print("Tổng của tất cả các ước của số đó là :" b)