print("Hãy nhập vào số thứ 1")
a=int(input())
print("Hãy nhập vào số thứ 2")
b=int(input())
print("Hãy nhập vào số thứ 3")
c=int(input())
while (a<=0 or b<=0 or c<=0):
	print("Nhập lại giá trị :")
	a = int(input())
	b = int(input())
	c = int(input())
if (a + b > c and a + c > b and b + c > a) :
	print("Đây là một tam giác")
	if(a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a) :
		print("Đây là một tam giác vuông")
	elif(a == b and b == c) :
		print("Đây là một tam giác đều")
	elif(a == b or a == c or b == c) :
		print("Đây là một tam giác cân")
	elif(a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b) :
		print("Đây là một tam giác tù")
	else :
		print("Đây là một tam giác nhọn")
else :
	print("Ba cạnh này không phải là ba cạnh của một tam giác")
