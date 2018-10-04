""" Funtions """

"""
   	A function is a block of code which performs a particular task
   	and it only runs when it is called.
	You can pass data, known as parameters, into a function.
"""

""" Define a function with no arguments and no return values """
def print_hello():
	print('Hello Python!')

""" Call the function """
print_hello()		# returns 'Hello Python!'




""" Functions with one argument and no return value """
def print_name(name):
	print(name)

""" Call the function """
print_name('Vinay Singh')	# returns 'Vinay Singh'




""" Functions with one argument and one return value """
def square_root(x):
	return x*x

""" Call function """
square = square_root(2)   # assigns 4 to square but it does not print
print(square)			# returns 4




""" define a function with two arguments (no default values) and """
""" one argument (has a default value) """
def my_calculator(x, y, operation='add'):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    else:
        print('valid operations are add and sub')

""" Function Call """
print(my_calculator(3, 5, 'add'))	# returns 8
print(my_calculator(3, 5))			# returns 8 because we have set default value of argument operation
print(my_calculator(5, 2, 'sub'))	# returns 3

