#!/usr/bin/python
"""
@author - sayantan
"""

from __future__ import print_function
import csv
import sys
import re

def read_vcf(vcf_file):
	f = open(vcf_file, 'r')
	for line in f.readlines():
		if line.startswith('##'):
			continue
		yield line

def pretty_print_progenity_vcf(data):
	i = 0
	for entry in data:
		i = i + 1
		print('\n')
		print("Variant number :", i)
		j = 0

		for key,value in entry.items():
			delimiter = ',' + entry['ALT']
			if key == 'INFO':
				progenity_details = ''.join(re.findall(r'^HGVS.+;', value))[:-1]
				snpeff = value.strip(progenity_details)
				snpeff_annotations = snpeff.split(delimiter)
				print(key + " : ")
				print('\t' + "Progenity HGVS :", progenity_details)
				print('\t' + "SnpEff Annotations :")
				for annotation in snpeff_annotations:
					j = j + 1
					print('\t\t' + "Annotation number :", j)
					print('\t\t' + annotation)
			else:
				print(key,":", value)
		print('\n')
		print('#'*50)

def main(input_file):
	global data
	data = csv.DictReader(read_vcf(input_file), delimiter='\t')
	pretty_print_progenity_vcf(data)

if __name__ == '__main__':
	main(sys.argv[1])

