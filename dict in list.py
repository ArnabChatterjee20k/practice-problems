l=[{1:0,2:6},{4:5,6:7},{8:7,9:68}]
k=[]
for i in l:
	for j in i.keys():
		k.append(j)
for i in l:
     	if l.index(i)!=0:
     		print("_______")
     	print("dict",i)
     	for j in k:
     	      if j in  i:
     	      	print("key",j)
     	      	print(i[j])