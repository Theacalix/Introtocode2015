startlist = range(101) 
print startlist

def fizzbuzz(x):

	if x % 3 == 0 and x % 5 == 0:
		return 'fizzbuzz'  
	elif x % 3 == 0: 
		return 'fizz' 
	elif x % 5 == 0: 
		return 'buzz' 
	else: 
		return x 

for x in startlist: 
	print fizzbuzz(x) 