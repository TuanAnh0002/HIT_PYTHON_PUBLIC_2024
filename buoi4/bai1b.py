n=int(input("Nhập số n :"))
while(n<7):
	print("Nhập lại giá trị n")
	n=int(input("Nhập số n :"))

test_list=[]
for i in range(0,n):
	test_list.append(int(input("Nhập vào :")))

insert_list=[8,5,4,0,1,3]
test_list[1:6]=insert_list
print(test_list)
MAX=test_list[0]
for i in range(1,n+1):
	if(MAX<test_list[i]):
		MAX=test_list[i]
print("Số lớn nhất trong list là :"MAX)
MIN=test_list[0]
for i in range(1,n+1):
	if(MIN>test_list[i]):
		MIN=test_list[i]
print("Số bé nhất trong list là :"MIN)
