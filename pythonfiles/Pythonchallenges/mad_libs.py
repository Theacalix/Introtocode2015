n = raw_input('What is your name? ').capitalize()
v = raw_input('Give me a movement verb. ').lower()
num = raw_input('Give me a number larger than 100. ')
c = raw_input('What is your favorite color? ').lower()
no = raw_input('What is your favorite food? ').lower()
adj = raw_input('How would you describe your favorite food? ').lower()
question_dict = {name: n, adjetive: adj, verb: v, number: num, color: c, noun: no}
print '''{name} was {verb} to the store.\nThey needed to buy {number} {color} carrots, {noun}, and {adjetive} bread.'''.format(**question_dict)
print '-'*75