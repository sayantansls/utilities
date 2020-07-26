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
START_THRESHOLD, DECREMENT = [85, 5]

def match_string(file_of_interest, threshold):
	isFound = 0
	print('INFO: Searching for file with {}% matching'.format(threshold))
	for file in files_list:
		file_basename = os.path.basename(file)
		match_ratio = fuzz.ratio(file_of_interest, file_basename)
		if match_ratio > threshold:
			locations_found.add(file)
			isFound = 1

	if isFound:
		print('INFO: Files found at {}% matching'.format(threshold))
		print('INFO: The file "{}" is present at {} locations'.format(file_of_interest, len(locations_found)))
		pprint(locations_found)
	else:
		print('INFO: No file found at {}% matching'.format(threshold))
		threshold = threshold - DECREMENT
		if threshold > 0:
			match_string(file_of_interest, threshold)
		else:
			print('FAIL: Exhausted all search options. File not found')

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

def main(file_of_interest):
	global locations_found
	locations_found = set()
	print('INFO: Searching for "{}" file'.format(file_of_interest))
	get_contents_of_dir(home)
	match_string(file_of_interest, START_THRESHOLD)
	print('\n')

if __name__ == '__main__':
	for input_file in sys.argv[1:]:
		main(input_file)