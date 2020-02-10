#!/usr/bin/python
"""
@author - sayantan
"""

from __future__ import print_function
import csv
import sys

def pretty_print_csv(inputfile):
	f = open(inputfile)
	data = csv.DictReader(f)
	i = 0
	for entry in data:
		i = i + 1
		print('\n')
		print("Row Number :", i)
		for key,value in entry.items():
			print(key, ":", value)
		print('\n')
		print('#'*50)

def main(inputfile):
	pretty_print_csv(inputfile)

if __name__ == '__main__':
	main(sys.argv[1])