input_list = raw_input("Give me a sentence.\n")

def oddlist(startlist):
	endlist = startlist[::2]
	return endlist

print oddlist(input_list) 