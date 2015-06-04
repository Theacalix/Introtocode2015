input_list = raw_input("Give me a word.\n")

def palindrometest(input_list):
	original = input_list
	palindrome = input_list[::-1]
	 
	if palindrome == original:
		print "Congradulations! Your word is a palindrome.\n"
	else: 
		print "Sorry, your word is not a palindrome.\n" 

palindrometest(input_list)

