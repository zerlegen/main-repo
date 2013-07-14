#!/usr/bin/python3

import shutil
import re
import os
import sys

################################################################################
#
# Analyzes a source tree for filenames in "camel case"  (that is, each word
# is capitalized with no characters between each word),
# then places each file with similar patterns into common lists
# 
# Since the list of filenames are initially sorted, it is enough to compare
# the first word in each filename.
#
################################################################################
#
# Given a source directory, analyze filenames based on camel case and
# return a list of lists, with each list element containing "similar" filenames 
# grouped together
#
# dir - the source directory to begin analysis
#
# RETURN: a list of lists, each list element containing a list of similar 
# filenames
#
################################################################################

def analyze_source(dir):
	result_list = []
	current_list = []
	file_list = os.listdir(dir)
	first_word_pattern = re.compile('^[A-Z][a-z0-9]*')
	current_match = ''
	for file in file_list:
		first_word = first_word_pattern.findall(file)
		if first_word != current_match:
			result_list.append(current_list)
			current_list = []
			current_match = first_word		
		current_list.append(file)
	
	return result_list

