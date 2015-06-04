range(num) #Gives a list counting from 0 with the number of items you put in 
            #Range can be used when you want something to loop a certain number of times 
a_list = [1, 2, 3] 
a_list = a_list + [4, 5] #this adds items to the list and updates the list to include the new items 
a_list.extend(range(6, 11) #this extends the list w/out a plus sign 
              #if adding to the range, start with the number 1 greater that the highest number in the previous list, and end with a number one greater than the number you want to end with 
len(a_list) #gives the length of each list               
alpha = list('abdef') #insert adds an item into the middle of the list 
alpha.insert(2, 'c')  #2 is the index you want to add at, and b is the item you want to put there 
print("\n Blah Blah") #\n puts what is printed on a new line 
while true: #creates a loop 
              if: #if blank is entered, this happens 
              break #ends the loop 
              elif: #however, if blank is entered, this other thing happens 
              continue #continues the loop
variable.lower() #makes all the letters lowercase 
variable.capitalize #capitalizes the first letter 
eff = alpha.pop() #removes the last item in the list (or the entered index number) and saves it
del = alpha(0) #removes the item at the index number 
alpha.remove(b) #removes the item by name or index number  
my_string = "This is my string." #anything in quotations \
my_string[0:3] #removes everything from index 0 to index 3 called a slice 
my_string[0:len(my_list)] #you have to go one past the last index number to get the end of the list
#this is equal to the len() of the list 
my_list[:2] #starts from the beginning and goes up to the number speficifed 
my_list[2:] #starts at the number speficifed and goes to the end 
my_list[:] #gives A COPY OF the entire list  \
my_list.sort() #puts the items in the list in order        
my_list[::2] #allows you to specify a 'step' 
my_list[::-1] #moves backwards through the list or string 
a_list[8:2:-1] #when counting backwards you have to reverse the order of the start and end 
a_list[-1] #gives you the index position for -1, or the very last number   
my_dic = {'name': 'Emily', 'job': 'cosplayer', 'projects': {'fancy': 'feferi', 'rave': ['noodle', 'cherry']}} #curly brackets and a colen denote dictionaries 
              #the first item is the key, and the second is the value
              #the order the keys are saved in changes 
my_dic['name'] #values have to be called by the name of the key 
              #values can be any variable type 
my_dic['projects']['rave'] #gives back the value of rave 
              #keys can be num, string, list, booleans 
profile= "Hi! My name is {name} and I live in {state}" #you can name placeholders  
profile.format(name='Emily', state='Oregon')   #to fill the placeholder, name of placeholder equals value 
profile_dict = {'name': 'Emily', 'state': 'Oregon'} 
profile.format(**profile_dict) #calls the keys and values in the dict and puts them in the function   
for thing in my_dic: 
  print(thing) #prints the key not the value
for key in my_dic:              
  print(my_dic[key]) #prints the value   
for value in my_dic.value():
              print(value) #does the same thing as above, but without the lookup 
#to run a file, save file and open in cmd 
#in cmd               
cd #changes directories 
cls #clears cmd               
              
             
              
           