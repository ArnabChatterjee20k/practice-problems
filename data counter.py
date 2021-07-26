l=[1,1,1,2,2,3,3,3]
a=[]
i=0
length=len(l)
while i<=length:
	print("data ",l[i],l.count(l[i]))
	print(i)
	i+=l.count(l[i])
	if i>=length:
		break