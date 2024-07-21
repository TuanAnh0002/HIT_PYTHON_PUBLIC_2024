print("Hãy nhập vào một số :")
a=int(input())
while (a<=0):
	print("Nhập lại giá trị :")
	a = int(input())

b = 0
while (a > 0):
	b = b + a % 10
	a = int(a / 10)


print("Tổng các chữ số của số đó : "b)
