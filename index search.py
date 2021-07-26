l=[1,1,1,2,2,3,3,3]
a=[]
i=0
length=len(l)
while i<=length:
	print("data ",l[i],l.count(l[i]))
	print(i)
	if i+l.count(l[i])==length:
		i+=l.count(l[i])-1
	else:
		i+=l.count(l[i])
j=0		
for i in range(length):
	print(l[i],)