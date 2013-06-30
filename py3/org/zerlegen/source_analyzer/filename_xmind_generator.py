#!/usr/bin/python3

import sys
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
################################################################################


fnAnalyzer = org.zerlegen.filename_analyzer.camelcase_analyzer
resultlist = fnAnalyzer.analyze_source_tree(sys.argv[1])
outMap = open(sys.argv[2], 'w')

# Generate the mind map:
xmind_API = org.zerlegen.pyXmind.xmind_xml

xmind_API.begin_map(outMap, "brainy.defaultGenre.simple")
xmind_API.begin_root(outMap, "org.xmind.ui.map.clockwise", "portecle")

foundresults = len(resultlist) > 0

if foundresults:
	print ("found results")
	xmind_API.begin_children(outMap)
	index = 1
	childstruct = "org.xmind.ui.map.logic.right"	
	for filegroup in resultlist:
		if len(filegroup) > 0:

			xmind_API.begin_node(outMap, childstruct, str(index))
			xmind_API.begin_children(outMap)

			for file in filegroup:
				xmind_API.begin_node(outMap, childstruct, file)
				xmind_API.end_node(outMap)

			xmind_API.end_children(outMap)
			xmind_API.end_node(outMap)
			index += 1
				 
				
	xmind_API.end_children(outMap)
else:
	print ("no results")




xmind_API.end_root(outMap)
xmind_API.end_map(outMap)

