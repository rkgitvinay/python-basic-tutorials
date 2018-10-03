""" List: Collection or Array """

"""
   Lists are just like the arrays declared in other languages, in which you
   can store multiple values in a single varible.
   In Python lists are written with square brackets.
   A single list can contain strings, integers, as well as objects
"""



""" Create a empty list """

my_list = []		
# OR
my_list = list()


""" Create List with initial values"""
my_list = [1,2,3,4]
print(my_list)		# returns [1,2,3,4]

print(my_list[0])	# returns 1
print(my_list[1])	# return 2
print(my_list[2])	# return 3
print(my_list[3])	# return 4



""" Modify a list with multiple operations """
my_list = []

my_list.append('Apple')	# appends 'Apple' in empty list
my_list.append('Bat')	# appends 'Bat' in empty list
my_list.append('Cat')    # appends 'Cat' in empty list

print(my_list) 			# return ['Apple', 'Bat', 'Cat']

print(my_list[1])		# returns 'Bat'


my_list.insert(0, 'Dog') # insert element 'Dog' at index 0
print(my_list) 			# return ['Dog','Apple', 'Bat', 'Cat']

my_list.remove('Cat') 	# finds first instance of 'Cat' and remove it
print(my_list) 			# return ['Dog','Apple', 'Bat']

my_list[0] = 'Bird'		# replace element 0 with 'Bird' 
print(my_list)			# return ['Bird','Apple', 'Bat', 'Cat']

