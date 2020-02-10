#!/usr/bin/python
"""
@author - sayantan
"""

from __future__ import print_function
import csv
import sys

def read_vcf(vcf_file):
	f = open(vcf_file, 'r')
	for line in f.readlines():
		if line.startswith('##'):
			continue
		yield line

def pretty_print_vcf(data):
	i = 0
	for entry in data:
		i = i + 1
		print('\n')
		print("Variant number :", i)

		for key,value in entry.items():
			print(key, ":", value)
		print('\n')
		print('#'*50)

def main(input_file):
	global data
	data = csv.DictReader(read_vcf(input_file), delimiter='\t')
	pretty_print_vcf(data)

if __name__ == '__main__':
	main(sys.argv[1])

