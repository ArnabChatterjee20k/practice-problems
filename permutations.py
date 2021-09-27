import math,random

word="abcd"
letter=[i for i in word]

#letters_to_combine=4
r=4
n=len(word)
ways=int(math.factorial(n)/math.factorial((n-r)))#int(ways) as we cant loop with float. Ways is float as we r getting its value by dividing certain values and implicitly value will be float.
#print(ways)

str_list=[]

print("main word",word)
for i in range(ways):
	letter_copy=letter.copy()
	str=""
	for j in range(r):
		try:
			rn=random.choice(letter_copy)
			str+=rn
			letter_copy.remove(rn)
		except Exception as e:
			print(e)
	str_list.append(str)
#	print(str)
print("total combinations with duplicates",len(str_list))

str_list.sort()
str_list=set(str_list)
print("total combinations without duplicates",len(str_list))#it will vary as it depends on number of duplicates generated
for i in str_list:
		print(i)
		

