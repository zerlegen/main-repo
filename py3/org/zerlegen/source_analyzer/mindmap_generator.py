#!/usr/bin/python3

import sys
import os
import java_analyzer.java_type_hierarchy
from   java_analyzer.java_type_hierarchy import JavaTypeHierarchy
import org.zerlegen.source_analyzer.filename_analyzer.camelcase_analyzer as camelcase_analyzer
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
# src_dir - source root directory
# dep_dir - dependency root directory
# out_map_name - output mindmap filename
#
#

def map_java_dir(src_dir, dep_dir, out_map_name):
    out_map = open(out_map_name, 'w')
    test_hier = JavaTypeHierarchy(src_dir, dep_dir)
    print("type_list: " + str(test_hier._type_list))
    print("roots: " + str(test_hier._roots))

    # start mind map
    #
    # write tree (node):
    #   begin node (node title)
    #       for all children
    #           write tree(current child)
    #       end node
    #
    # for all roots:
    #   write tree(root node i)

    # start mind map
    xmind_API = org.zerlegen.pyXmind.xmind_xml
    xmind_API.begin_map(out_map, "brainy.defaultGenre.simple")
    xmind_API.begin_root(out_map, "org.xmind.ui.logic.right", src_dir)
    xmind_API.begin_children(out_map)

    def traverse(node_id):
        print("traverse node_id : " + str(node_id))
        name = test_hier.get_node_name(node_id)
#        print("begin node: " + name)
      
        xmind_API.begin_node(out_map, "org.xmind.ui.logic.right", name)
        children = test_hier.get_children(node_id)
        
      
        if len(children) > 0:
            xmind_API.begin_children(out_map)

        for child in children:
            traverse(hash(child))

        if len(children) > 0:
            xmind_API.end_children(out_map)

        xmind_API.end_node(out_map)
#        print("end node: " + name)

    #print("roots: " + test_hier._roots)

    for root_id in test_hier.get_root_nodes():
        traverse(root_id)

    xmind_API.end_children(out_map)
    xmind_API.end_root(out_map)
    xmind_API.end_map(out_map, "java_type_analysis")
    out_map.close()



################################################################################
#
# Analyze files in a given directory for similar filenames and generate the 
# resulting XMind mind map. This method only analyzes
# the specified directory.  It is left to the caller to make repeated calls for
# subdirs.
#
# src_dir: directory whose files to analyze
# is_root: specifies whether we're mapping the root directory of the tree
# 	   (requires separate pyXMind calls)
# 
#
################################################################################

def fn_map_dir(src_dir, is_root, out_map):

	# Have directory analyzed
	#fn_analyzer = org.zerlegen.filename_analyzer.camelcase_analyzer
	result_list = camelcase_analyzer.analyze_source(src_dir)
	
	# Generate the mind map:
	xmind_API = org.zerlegen.pyXmind.xmind_xml
	
	if (is_root):
		xmind_API.begin_map(out_map, "brainy.defaultGenre.simple")
		xmind_API.begin_root(out_map, "org.xmind.ui.logic.right", src_dir)
#		print("Creating root node...")		
	else:
		xmind_API.begin_node(out_map, "org.xmind.ui.logic.right", 
				     os.path.basename(src_dir))
#		print("Creating subdir node...")
	foundresults = len(result_list) > 0

	if foundresults:
#		print ("found results")
		xmind_API.begin_children(out_map)
		index = 1
		childstruct = "org.xmind.ui.map.logic.right"	
		for filegroup in result_list:
			if len(filegroup) > 0:
				xmind_API.begin_node(out_map, childstruct, str(index))
				xmind_API.begin_children(out_map)
	
				for file in filegroup:
			
					# If this file is a dir, scan sub dirs
					full_path = os.path.join(src_dir, file)

					if os.path.isdir(full_path):
						fn_map_dir(full_path, False, out_map)
					else:
						xmind_API.begin_node(out_map, 
								     childstruct, file)
#						print("Creating leaf node: " + file)
						xmind_API.end_node(out_map)
	
				xmind_API.end_children(out_map)
				xmind_API.end_node(out_map)
				index += 1
		xmind_API.end_children(out_map)
	#else:
#		print ("no results")

	if (is_root):
		xmind_API.end_root(out_map)
		xmind_API.end_map(out_map, "filename_analysis")
	else:
		xmind_API.end_node(out_map)
################################################################################

map_java_dir('/home/epom/test-repo/portecle/src/main/net/sf/portecle/', 
             '/cygdrive/c/Program Files (x86)/Java/jre6/lib',
             '/home/epom/test-repo/py3/org/zerlegen/pyXmind/build/content-in.xml')

#fn_map_dir(sys.argv[1], True, open(sys.argv[2], 'w'))
