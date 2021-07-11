while True:
	n=int(input("Enter the number "))	
	if n%(n//2)==0:
		print("No")
	elif n%(n//2)!=0:
		print("Yes")