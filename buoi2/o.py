print("Nhập vào số n")
a=int(input())
b = 0
c = 0
for i in range (1,a+1) :
	while (a > 0):
		b = b + a % 10
		c = c + b ** 3
		a = int(a / 10)
if c == a :
	print()
else :
	print()


