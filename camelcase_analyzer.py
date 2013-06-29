#!/usr/bin/python3

import shutil
import re
import os
import sys

################################################################################

# Analyzes a source tree for filenames in "camel case"  (that is, each word
# is capitalized with no characters between each word),
# then places each file with similar patterns into common lists
# 
# Since the list of filenames are initially sorted, it is enough to compare
# the first word in each filename.

################################################################################

def analyze_source_tree(root_dir):
	resultlist = []
	currentlist = []
	filelist = os.listdir(root_dir)
	firstwordpattern = re.compile('^[A-Z][a-z0-9]*')
	currentmatch = ''
	for file in filelist:
		firstword = firstwordpattern.findall(file)
		if firstword != currentmatch:
			resultlist.append(currentlist)
			currentlist = []
			currentmatch = firstword		
		currentlist.append(file)
	
	print("Results:")
	for sublist in resultlist:
		print (sublist)


