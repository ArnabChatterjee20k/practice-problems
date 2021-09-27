a=[]
b=[1,23,162,11,2,1,33		]
print(b)
n=int(input("Input position to be removed"))

def my_func(b):
	# n will be equal to n-1 index
	for i in b:
		if b.index(i)!=n-1:
			a.append(i)
	print(a)
	return a
	
def another(b):
	a=b
	a.pop(n-1)
	print(a)
	return a
	
	
if n<=len(b):
	my_func(b)
	another(b)
else:
	print("Error")


	