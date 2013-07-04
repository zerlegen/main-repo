#!/usr/bin/python3

import sys
import os
import org.zerlegen.filename_analyzer.camelcase_analyzer
import org.zerlegen.pyXmind.xmind_xml

# begin_map(outFile, theme)
# begin_root(outFile, structure, title)
# end_root(outFile)
# begin_children(outFile)
# end_children(outFile)
# begin_node(outFile, structure, title)
# end_node(outFile)
# end_map(outFile)

################################################################################
#
# Analyzes a source tree based on similar file names, and generates an xmind
# mind map grouping these similar files together
#
# sys.argv[1] - root source directory
# sys.argv[2] - output file containing the resulting xml
# 
# Uses the following methods in the "pyXmind" module:
#
# begin_map(outFile, theme)
# begin_root(outFile, structure, title)
# end_root(outFile)
# begin_children(outFile)
# end_children(outFile)
# begin_node(outFile, structure, title)
# end_node(outFile)
# end_map(outFile)
#
################################################################################
#
# Analyze files in a given directory for similar filenames and generate the 
# resulting XMind mind map. This method only analyzes
# the specified directory.  It is left to the caller to make repeated calls for
# subdirs.
#
# in_dir: directory whose files to analyze
# is_root: specifies whether we're mapping the root directory of the tree
# 	   (requires separate pyXMind calls)
# 
#
################################################################################

def map_dir(in_dir, is_root, out_map):

	# Have directory analyzed
	fn_analyzer = org.zerlegen.filename_analyzer.camelcase_analyzer
	result_list = fn_analyzer.analyze_source(in_dir)
	
	# Generate the mind map:
	xmind_API = org.zerlegen.pyXmind.xmind_xml
	
	if (is_root):
		xmind_API.begin_map(out_map, "brainy.defaultGenre.simple")
		xmind_API.begin_root(out_map, "org.xmind.ui.map.clockwise", in_dir)
		print("Creating root node...")		
	else:
		xmind_API.begin_node(out_map, "org.xmind.ui.logic.right", 
				     os.path.basename(in_dir))
		print("Creating subdir node...")
	foundresults = len(result_list) > 0

	if foundresults:
		print ("found results")
		xmind_API.begin_children(out_map)
		index = 1
		childstruct = "org.xmind.ui.map.logic.right"	
		for filegroup in result_list:
			if len(filegroup) > 0:
				xmind_API.begin_node(out_map, childstruct, str(index))
				xmind_API.begin_children(out_map)
	
				for file in filegroup:
			
					# If this file is a dir, scan sub dirs
					full_path = os.path.join(in_dir, file)

					if os.path.isdir(full_path):
						map_dir(full_path, False, out_map)
					else:
						xmind_API.begin_node(out_map, 
								     childstruct, file)
						print("Creating leaf node: " + file)
						xmind_API.end_node(out_map)
	
				xmind_API.end_children(out_map)
				xmind_API.end_node(out_map)
				index += 1
		xmind_API.end_children(out_map)
	else:
		print ("no results")

	if (is_root):
		xmind_API.end_root(out_map)
		xmind_API.end_map(out_map, "filename_analysis")
	else:
		xmind_API.end_node(out_map)
################################################################################

map_dir(sys.argv[1], True, open(sys.argv[2], 'w'))
