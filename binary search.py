l=[3,1,17,88,6,0,2,2,4,6,7,537,33,7,33,31,1,2,71,9,100]
# to delete if same elements present
list=[]
for i in l:
	if i not in list:
		list.append(i)
# sorting the list
list.sort()
print(list)
#getting the median value index and rounding the number if data type of median is float
median=int(len(list)/2)
a=int(input("Enter the no.:  "))

if a>list[median]:
	for i in list[median:len(list)+1]:
		if i==a:
			print("index:",list.index(i))
elif a<list[median]:
	for i in list[:median+1]:
		if i==a:
			print("index:",list.index(i))
elif list[median]==a:
	print(median)
else:
	print("Not present")