s1=[]
s2=[]
n=int(input("Nhập số phần tử của S1 :"))
m=int(input("Nhập số phần tử của S2 :"))
for i in range(0,n):
	s1.append(int(input(f'a[{i}]=')))
for i in range(0,m):
	s2.append(int(input(f'b[{i}]=')))
s1_dao=s1[::-1]
print("Đảo ngược của S1 là :",s1_dao)
a=int(input("Nhập số a :"))
b=int(input("Nhập số b :"))
while(a < 1 or a >= b or b > len(s2)):
	a=int(input("Nhập số a :"))
	b=int(input("Nhập số b :"))
s2_dao=s2[b:a-1:-1]
s2[a:b+1]=s2_dao
print("Chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b là :",s2)
c=len(s1)//2
for i in range (0,c) : 
	s1=s1[:i]+s1[i+1:]
	s3=s1
print(" các kí tự vị trí chẵn là : ",s3)
