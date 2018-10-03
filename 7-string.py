""" String """

"""
   String variables in python are surrounded by either single quotation marks,
   or double quotation marks
"""

""" Create a string variable """
my_string = 'Hello World'
print(my_string) 		# returns 'Hello World'


""" Examine a string variable"""
print(my_string[0])		# returns 'H'

string_length = len(my_string) 	# len function returns length of string variable
print(string_length)	# returns 11


""" Basic string operations """
my_lower = my_string.lower()           # sets all characters in lower case
print(my_lower)			# returns 'hello world'

my_upper = my_string.upper()   # sets all characters in upper case
print(my_upper)				# returns 'HELLO WORLD'


my_index = my_string.find('Hello')      # returns index of first occurrence of given string
print(my_index)						# returns 0

my_index = my_string.find('like')      # returns index of first occurrence of given string
print(my_index) 		# returns -1 since string does't contain word 'like'


my_replace = my_string.replace('World', 'Vinay')    # replaces all instances of 'World' with 'Vinay'
print(my_replace)		# returns 'Hello Vinay'