import random 
number =random.randint(1, 50)
print number 

user_guess = input('Guess a number between 1 and 50. ')


while user_guess != number: 
	if  user_guess < number: 
		print 'Try again! The number I am thinking of is higher than {}'.format(user_guess)
		user_guess = input('Guess again.\n')
		#print user_guess 
	elif  user_guess > number: 
		print 'Try again! The number I am thinking of is lower than {}'.format(user_guess)
		user_guess = input('Guess again.\n')
		#print user_guess
else:
	user_guess == number
	print 'Congradulations! The number was {}'.format(number)





