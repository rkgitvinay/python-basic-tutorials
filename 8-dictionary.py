""" Dictionary """

"""
   Dictionary is a collection of key-value pairs.
   keys must be unique, and can be strings, numbers, or tuples.
   values can be any type.
"""

""" Create an empty dictionary """
empty_dict = {}
#OR
empty_dict = dict()


""" Create a dictionary """
my_info = {'name':'Vinay Singh', 'city':'Allahabad','pin':323232}
#OR
my_info =  dict(name='Vinay Singh', city='Allahabad', pin=323232)


""" Access a dictionary """
print(my_info['name'])		# returns 'Vinay Singh'

print(len(my_info))         # returns 3

check_key = 'name' in my_info  #(only checks keys)
print(check_key)			# returns True


""" Modify a dictionary """
my_info['gender'] = 'Male'	# add a new entry
print(my_info)				# returns {'name': 'Vinay Singh', 'city': 'Allahabad', 'pin': 323232, 'gender': 'Male'}

my_info['city'] = 'Noida'	# edit an existing entry
print(my_info)				# returns {'name': 'Vinay Singh', 'city': 'Noida', 'pin': 323232, 'gender': 'Male'}

del my_info['pin']			# delete an entry
print(my_info) 				# returns {'name': 'Vinay Singh', 'city': 'Noida', 'gender': 'Male'}
	