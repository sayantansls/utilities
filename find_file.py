#!/usr/bin/python

"""
author : sayantan
This script consumes a file and searches for it in the entire HOME.
"""

import os, sys
from pprint import pprint
from fuzzywuzzy import fuzz

files_list = list()
home = os.path.expanduser("~")
threshold = 60

def get_contents_of_dir(directory):
	contents = os.listdir(directory)
	for content in contents:
		content_path = os.path.join(directory, content)
		if os.path.isdir(content_path):
			#ignores the hidden files (beginning with a period)
			if not content[0] == '.': 
				get_contents_of_dir(content_path)
		elif os.path.isfile(content_path):
			files_list.append(content_path)

def main(file_name):
	get_contents_of_dir(home)
	isFound, locations_found = [0, set()]
	for file in files_list:
		file_basename = os.path.basename(file)
		match_ratio = fuzz.ratio(file_name, file_basename)
		if match_ratio > threshold:
			isFound = 1
			locations_found.add(file)
			#print(file_name, file_basename, match_ratio)

	print('INFO: Searching for similar files with string matching....')
	print('INFO: File names with greater than {}% matching are considered'.format(threshold))

	if isFound:
		print('INFO: File searched for is FOUND')
		print('INFO: The file "{}" is present at {} locations'.format(file_name, len(locations_found)))
		pprint(locations_found)
	else:
		print('INFO: The file {} is not found'.format(file_name))

if __name__ == '__main__':
	main(sys.argv[1])