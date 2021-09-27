n=int(input ("n"))
a=0
c=0
m=n
while a==0:
	n=n//10
	c+=1
	if n==0:
		a=1
print(c)

k=0
print(m)
for i in range(c):
	k+=m%10
	m=m//10
print(k)
	