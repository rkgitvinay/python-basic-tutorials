""" Tuple """

"""
   A tuple is a collection like list which is ordered but unchangeable. 
   In Python tuples are written with round brackets.
"""

""" create a tuple """
my_tuple = ('apple', 'banana', 'orange')
print(my_tuple)			# returns ('apple', 'banana', 'orange')


""" Access tuple items """
print(my_tuple[0])		# returns apple

tuple_length = len(my_tuple) 	# len function returns length of a list Or number of items in a list
print(tuple_length)		# return 3

# my_tuple[2] = 2       # throws an error because elements of a tuple cannot be modified


""" Operations of tuple """
my_tuple = my_tuple + ('cherry','mango')  # appends 'cherry' and 'mango' in tuple
print(my_tuple) 		# returns ('apple', 'banana', 'orange', 'cherry', 'mango')

