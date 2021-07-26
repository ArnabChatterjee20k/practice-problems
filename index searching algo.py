l=[1,1,4,2,2,3,3,3]
l.sort()
a={}
b={}
i=0
length=len(l)
while i<=length:
	a[l[i]]=[i+1,i+l.count(l[i])]
	b[l[i]]=[i,i+l.count(l[i])-1]
	i+=l.count(l[i])
	if i>=length:
		break
print(l)
print("Details of data present")
print()
print("position",a)
print()
print("index",b)