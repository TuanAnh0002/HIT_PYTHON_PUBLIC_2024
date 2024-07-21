print("Nhập vào số n")
a=int(input())
tong = 1
hieu = 0
for i in range (2,2 * a + 2	) :
	if i % 2 != 0 :
		tong = tong + i  

for i in range (1,2 * a + 2) :
	if i % 2 == 0 :
		hieu = hieu - i

print("Gía trị của biểu thức S câu a là ", tong + hieu)

tong_b = 0
for i in range (1,a + 1):
	tong_b = tong_b + ( 1 / i )

print("Gía trị của biểu thức S câu b là"tong_b)
