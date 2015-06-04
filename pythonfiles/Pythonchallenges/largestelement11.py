num_list = [3, 7, 2, 10, 14, 5]


def largest_element(input_list): 
	largest_num = 0 
	for x in input_list:    
		if x > largest_num:
			largest_num = x 
			#print largest_num  

	return largest_num 

print largest_element(num_list) 
