a=int(input("Số bạn tham gia kiểm tra là :"))
d=[]
e=[]
for i in range(a):
	c=input("Tên bạn :")
	e.append(c)
	b=int(input("Số điểm bạn đạt được là :"))
	d.append(b)

f=min(d)
for i in range(a):
	if(f==d[i]):
		print("Bạn có số điểm thấp nhất là :",e[i])
