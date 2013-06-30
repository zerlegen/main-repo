#!/usr/bin/python3

###############################################################################
# Allows generating XML for an XMind mind map tree in a depth-first fashion.
###############################################################################

import time
import sys

###############################################################################
# Low-lever write functions - don't use these unless you want to write custom 
# XML
###############################################################################

def write_XMIND_HEADER(outFile, encoding="UTF-8"):
	outFile.write("<?xml version=\"1.0\" encoding=\"" + encoding + 
		      "\"standalone=\"no\"?>")
		     
def write_XMIND_TITLE(outFile,  text):
	outFile.write("<title>" + text + "</title>")

def write_XMIND_XMAP_CONTENT_OPEN(outFile, timestamp):
	outFile.write(
	"<xmap-content xmlns=\"urn:xmind:xmap:xmlns:content:2.0\" " +
	"xmlns:fo=\"http://www.w3.org/1999/XSL/Format\" " + 
	"xmlns:svg=\"http://www.w3.org/2000/svg\" " +
	"xmlns:xhtml=\"http://www.w3.org/1999/xhtml\" " + 
	"xmlns:xlink=\"http://www.w3.org/1999/xlink\" " +
	"timestamp=\"" + timestamp + "\" version=\"2.0\">")

def write_XMIND_XMAP_CONTENT_CLOSE(outFile):
	outFile.write("</xmap-content>")

def write_XMIND_SHEET_OPEN(outFile, theme, timestamp):
	outFile.write("<sheet id=\"5beq22t1dt6hg5qhtceovobls2\" theme=\"" + 
			theme + "\" timestamp=\"" + timestamp + "\">")

def write_XMIND_SHEET_CLOSE(outFile):
	outFile.write("</sheet>")

def write_XMIND_TOPICS_OPEN(outFile):
	outFile.write("<topics type=\"attached\">")

def write_XMIND_TOPICS_CLOSE(outFile):
	outFile.write("</topics>")


def write_XMIND_TOPIC_OPEN(outFile, structure, timestamp):
	outFile.write("<topic id=\"5jlu3jotvfr94mnaran8caioqv\"" + 
		      " structure-class=\"" + structure + "\" timestamp=\"" + 
                      timestamp + "\">")

# use to add child nodes - these don't take maps as structures
def write_XMIND_TOPIC_OPEN(outFile, structure, timestamp):
	outFile.write("<topic id=\"5jlu3jotvfr94mnaran8caioqv\"" + 
		      " structure-class=\"" + structure + "\" timestamp=\"" + 
                      timestamp + "\">")

def write_XMIND_TOPIC_CLOSE(outFile):
	outFile.write("</topic>")

def write_XMIND_CHILDREN_OPEN(outFile):
	outFile.write("<children>")

def write_XMIND_CHILDREN_CLOSE(outFile):
	outFile.write("</children>")

def generate_xmind_timestamp():
	return (str(int(time.time()) * 1000))


###############################################################################
# High level methods:
# 
# These methods allow generating an XMind mind map tree in a depth-first
# fashion.  First, the map and root node are initialized with the following 
# calls:
#
# 	begin_map()
# 	begin_root()
# 
# To insert child nodes, call:
#
# 	begin_children()
#
# followed by one or more sequences of:
#   
# 	begin_node()
#	end_node()
#
# When all children are inserted, call:
#
# 	end_children()
# 
# When all root children are inserted, call:
#	
#	end_root()
#	end_map()
#
# To insert grandchildren or lower nodes, nest the sequuence of:
#
# 	begin_children()
#	begin_node()
#	end_node()
#	end_children()
#
# BETWEEN the begin_node() and end_node() calls of the node's parent.  
#
# For example, these calls will create a tree with a root node and 2 child nodes,
# with the first child having its own child (indentation added for clarity):
#
# 	begin_map()
#	begin_root()
#	begin_children()
#		begin_node()
#		begin_children()
#			begin_node()
#			end_node()
#		end_children()
#		end_node()
#		begin_node()
#		end_node()
#	end_children()
# 	end_root()
# 	end_map()
#
###############################################################################

def begin_map(outFile, theme):
	write_XMIND_HEADER(outFile)
	write_XMIND_XMAP_CONTENT_OPEN(outFile, generate_xmind_timestamp())
	write_XMIND_SHEET_OPEN(outFile, theme, generate_xmind_timestamp())

def begin_root(outFile, structure, title):
	write_XMIND_TOPIC_OPEN(outFile, structure, generate_xmind_timestamp())
	write_XMIND_TITLE(outFile, title)

def end_root(outFile):
	write_XMIND_TOPIC_CLOSE(outFile)

def begin_children(outFile):
	write_XMIND_CHILDREN_OPEN(outFile)
	write_XMIND_TOPICS_OPEN(outFile)

def end_children(outFile):
	write_XMIND_TOPICS_CLOSE(outFile)
	write_XMIND_CHILDREN_CLOSE(outFile)


def begin_node(outFile, structure, title):
	write_XMIND_TOPIC_OPEN(outFile, structure, generate_xmind_timestamp())
	write_XMIND_TITLE(outFile, title)

def end_node(outFile):
	write_XMIND_TOPIC_CLOSE(outFile)


def end_map(outFile):
	write_XMIND_TITLE(outFile, "Sheet 1")
	write_XMIND_SHEET_CLOSE(outFile)
	write_XMIND_XMAP_CONTENT_CLOSE(outFile)
	outFile.close()

###############################################################################
# Unit Tests:
###############################################################################

def test_two_children_four_grandchildren():

	XMIND_STRUCT_LOGIC_RIGHT = "org.xmind.ui.logic.right"
	XMIND_STRUCT_MAP_CLOCKWISE = "org.xmind.ui.map.clockwise"

	outFile = sys.stdout
	begin_map(outFile, "brainy.defaultGenre.simple")

	# root node
	begin_root(outFile, XMIND_STRUCT_MAP_CLOCKWISE, "root node")
	begin_children(outFile)
	
	# first child	
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "child1")

	# 3 grandchildren off child 1
	begin_children(outFile)
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild")
	end_node(outFile)
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild2")
	end_node(outFile)
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild3")
	end_node(outFile)
	end_children(outFile)
	end_node(outFile)

	# second child	
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "child2")
	begin_children(outFile)
	begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild4")
	end_node(outFile)
	end_children(outFile)
	end_node(outFile)
	end_children(outFile)

	# finish	
	end_root(outFile)
	end_map(outFile)
	
	outFile.close()


###############################################################################


