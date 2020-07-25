#!/usr/bin/python

"""
author : sayantan
The script consumes a file and changes the filename to a proper name with hyphen
'Test File.txt' ---> test-file.txt
"""

import os, sys

def change_name_command(input_path):
	original_dirname = os.path.basename(os.path.normpath(input_path))
	final_dirname = original_dirname.lower().replace(' ', '-')
	final_path = input_path.replace(original_dirname, final_dirname)
	command = 'mv "{}" {}'.format(input_path, final_path)
	print('INFO: Original File/directory name : {}'.format(original_dirname))
	print('INFO: Final File/directory name : {}'.format(final_dirname))

	return command

def main(input_path):
	if os.path.isdir(input_path):
		print('INFO: {} is a directory'.format(input_path))
		command = change_name_command(input_path)
		os.system(command)

	elif os.path.isfile(input_path):
		print('INFO: {} is a file'.format(input_path))
		command = change_name_command(input_path)
		os.system(command)

	else:
		print('WARN: FILE/DIR DOES NOT EXIST')

if __name__ == '__main__':
	for file in sys.argv[1:]:
		main(file)