print("Nhap vao n :")
n=int(input())
for a in range(1,n+1) :
	S=0
	for b in range(1,a) :
		if (a % b == 0) : 
			S+=b
	for c in range(a+1,n+1) :
		H=0
		for d in range(1,c) :
			if (c % d == 0) : 
				H+=d
				if (S==c and H==a) :
					print(a,c,end=" ")
