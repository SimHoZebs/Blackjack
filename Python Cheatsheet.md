# Sim's Python Cheatsheet

###### Type
```python 
#String

type_to_string_conversion = str( argument )

str.find('string', start, end)

str.replace('string_to_replace','new_string_in_place', count)

list_words_from_a_string = string.split('separator', count)

str[position].lower()
# lower can be replace with upper

def find_alphabets_in_string(string):
	str_detector = "abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-=]}{[\|;:'\",<.>/? "
# Returns boolean value in if a string contains any alphabets in "alphabets".

f"This is f-string formatting using {variable}"
     
#Boolean
123

variable_to_string_conversion = bool( argument )
# If ( arugment ) == (), (False), (0), result is False. Else is True. 
```

###### list
```python
list( argument )
# makes a list out of iterable argument. 
# Example: list('')

a_list = [element for element in condition]
# makes a_list a list of elements from an iterable parameter
# Example: [element for element in range(0, 100)]

zip(list1, list2, more_lists)
# Combines elements to a tuple

new_list = []
for item1, item2 in list_with_two_item_tuple:
	new_list.append(item1)
	new_list.append(item2)
#Primitive way to unpack a 2 item tuple list

a_list[enumerate(iterable)]
# Makes a_list a list of tuples of number counting up and the iterable
# Example: [enumerate('Te')] 
# >> [(0, 'T'), (1, 'e')]
```

###### for and while loops
```python
for item1, item2 in list_with_tuples:
	parameter1(item1)
	parameter2(item2)
```
###### Misc.
```python
def function(*args, **kwargs):
	command line

# *args allows infinite arguments as input and puts them in a tuple.
# **kwargs allows infinite key = item as input and puts them in a dictionary.

len(string)
#Returns the number of characters in string

map(function, list_of_arguments)
#runs each arguments consecutively in function and saves it. Compact version of while loop. Must be ran within list to see results.

filter(function, list_of_arguments)
#runs each arguments consecutively in function and save only true outputs. Compact version of while loop. Must be ran within list to see results.

lambda

reversed()

```

###### msvcrt library
```python
msvcrt.getch()
# returns keypress. Must convert to str to use. Only works in cmd
```

###### Class
```python
class ClassName:

	object_attribute = 'some value'

	def __init__(self, argument1):
		# This creates attributes (ex. type) for the class
		# Argument is not neccessary but if you write it it becomes a must input
		self.argument = argument
		# h

	def method(self, argument2):
		# This creates functions for the class
		print(f'{self.argument1} must be called with self but not {argument2}')
		# The argument can be named the same; they are separated by being called from self. and not. But doing so could cause confusion.

class ClassName2(ClassName):
	# Inheritance; copies all def & attributes over.

	def __init__(self, argument):
		# Creating ClassName2's own def functions overwrites inherited ones, unless a line like below is written.
		ClassName.__init__(self, "argument")
		# Argument for ClassName.__init__ can only be declared within ClassName2
		
```

##### Linting and Testing
```python
import unittest
import py_file_for_test

class Test(unittest.TestCase):

	def test_name(self):
		some_argument = 'Could be a text'
		result = py_file_for_test.function(some_argument)
		self.assertEqual(reuslt, 'wanted_result')

if __name__ == '__main__':
	unittest.main()
```