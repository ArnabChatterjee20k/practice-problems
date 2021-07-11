from PyDictionary import PyDictionary
while True:
	
	a=input('word:\t')
	try:
		(PyDictionary(a).printMeanings())
	except Exception as e :
		print('not found')
		print(e)
	print()