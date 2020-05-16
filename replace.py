#!/usr/bin/env python

'''replace.py: Add replacement functions in strings.

Add functions mostly related to the variables strings
and to replace strings in it, with general formats.

Functions:
to_array(string) 		-- converts string to an array
comma_to_point(string)	-- replaces the commas with points
point_to_comma(string)	-- replaces the points with commas
'''

__author__ = "LuckJMG"
__copyright__ = "Copyright 2020, LuckJMG"
__credits__ = ["LuckJMG"]

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "LuckJMG"
__email__ = "lucas.mosquera13@gmail.com"
__status__ = "Production"

def to_array(string):
	"""Converts a string to an array.

	Converts a string to an array relative to its spaces.

	Parameters:
	string -- string to be converted to an array

	Exceptions:
	Return None -- if no spaces in the string
	"""

	new_array = string.split(' ')		# Convert the string into array
	return new_array					# Return the new array

def comma_to_point(string):
	'''Replaces the commas with points.

	Replaces all the commas in a string with points.

	Parameters:
	string -- string where replace the commas with points
	'''

	string = string.replace(',', '.')	# Replace the commas with points in string
	return string						# Return the new string

def point_to_comma(string):
	'''Replaces the points with commas.

	Replaces all the points in a string with commas.

	Parameters:
	string -- string where replace the points with commas
	'''

	string = string.replace('.', ',')	# Replace the points with commas in string
	return string						# Return the new string