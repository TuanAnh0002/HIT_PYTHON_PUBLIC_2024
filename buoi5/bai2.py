a=int(input("Nhập số điểm X :"))
while (a<1 or a>1000):
	print("Nhập lại giá trị X:")
	a=int(input())

if(a<=3):
	print("Số bước tối thiểu là :",1)
elif(a%3==0):
	print("Số bước tối thiểu là :",a/3)
else:
	print("Số bước tối thiểu là :",a//3+1)

