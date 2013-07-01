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

def write_XMIND_HEADER(out_file, encoding="UTF-8"):
	out_file.write("<?xml version=\"1.0\" encoding=\"" + encoding + 
		      "\"" + " standalone=\"no\"?>")
		     
def write_XMIND_TITLE(out_file,  text):
	out_file.write("<title>" + text + "</title>")

def write_XMIND_XMAP_CONTENT_OPEN(out_file, timestamp):
	out_file.write(
	"<xmap-content xmlns=\"urn:xmind:xmap:xmlns:content:2.0\" " +
	"xmlns:fo=\"http://www.w3.org/1999/XSL/Format\" " + 
	"xmlns:svg=\"http://www.w3.org/2000/svg\" " +
	"xmlns:xhtml=\"http://www.w3.org/1999/xhtml\" " + 
	"xmlns:xlink=\"http://www.w3.org/1999/xlink\" " +
	"timestamp=\"" + timestamp + "\" version=\"2.0\">")

def write_XMIND_XMAP_CONTENT_CLOSE(out_file):
	out_file.write("</xmap-content>")

def write_XMIND_SHEET_OPEN(out_file, theme, timestamp):
	out_file.write("<sheet id=\"5beq22t1dt6hg5qhtceovobls2\" theme=\"" + 
			theme + "\" timestamp=\"" + timestamp + "\">")

def write_XMIND_SHEET_CLOSE(out_file):
	out_file.write("</sheet>")

def write_XMIND_TOPICS_OPEN(out_file):
	out_file.write("<topics type=\"attached\">")

def write_XMIND_TOPICS_CLOSE(out_file):
	out_file.write("</topics>")


def write_XMIND_TOPIC_OPEN(out_file, structure, timestamp):
	out_file.write("<topic id=\"5jlu3jotvfr94mnaran8caioqv\"" + 
		      " structure-class=\"" + structure + "\" timestamp=\"" + 
                      timestamp + "\">")

# use to add child nodes - these don't take maps as structures
def write_XMIND_TOPIC_OPEN(out_file, structure, timestamp):
	out_file.write("<topic id=\"5jlu3jotvfr94mnaran8caioqv\"" + 
		      " structure-class=\"" + structure + "\" timestamp=\"" + 
                      timestamp + "\">")

def write_XMIND_TOPIC_CLOSE(out_file):
	out_file.write("</topic>")

def write_XMIND_CHILDREN_OPEN(out_file):
	out_file.write("<children>")

def write_XMIND_CHILDREN_CLOSE(out_file):
	out_file.write("</children>")

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

def begin_map(out_file, theme):
	write_XMIND_HEADER(out_file)
	write_XMIND_XMAP_CONTENT_OPEN(out_file, generate_xmind_timestamp())
	write_XMIND_SHEET_OPEN(out_file, theme, generate_xmind_timestamp())

def begin_root(out_file, structure, title):
	write_XMIND_TOPIC_OPEN(out_file, structure, generate_xmind_timestamp())
	write_XMIND_TITLE(out_file, title)

def end_root(out_file):
	write_XMIND_TOPIC_CLOSE(out_file)

def begin_children(out_file):
	write_XMIND_CHILDREN_OPEN(out_file)
	write_XMIND_TOPICS_OPEN(out_file)

def end_children(out_file):
	write_XMIND_TOPICS_CLOSE(out_file)
	write_XMIND_CHILDREN_CLOSE(out_file)


def begin_node(out_file, structure, title):
	write_XMIND_TOPIC_OPEN(out_file, structure, generate_xmind_timestamp())
	write_XMIND_TITLE(out_file, title)

def end_node(out_file):
	write_XMIND_TOPIC_CLOSE(out_file)


def end_map(out_file, sheet_name):
	write_XMIND_TITLE(out_file, sheet_name)
	write_XMIND_SHEET_CLOSE(out_file)
	write_XMIND_XMAP_CONTENT_CLOSE(out_file)
	out_file.close()

###############################################################################
# Unit Tests:
###############################################################################

def test_two_children_four_grandchildren():

	XMIND_STRUCT_LOGIC_RIGHT = "org.xmind.ui.logic.right"
	XMIND_STRUCT_MAP_CLOCKWISE = "org.xmind.ui.map.clockwise"

	out_file = sys.stdout
	begin_map(out_file, "brainy.defaultGenre.simple")

	# root node
	begin_root(out_file, XMIND_STRUCT_MAP_CLOCKWISE, "root node")
	begin_children(out_file)
	
	# first child	
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "child1")

	# 3 grandchildren off child 1
	begin_children(out_file)
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "grandchild")
	end_node(out_file)
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "grandchild2")
	end_node(out_file)
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "grandchild3")
	end_node(out_file)
	end_children(out_file)
	end_node(out_file)

	# second child	
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "child2")
	begin_children(out_file)
	begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "grandchild4")
	end_node(out_file)
	end_children(out_file)
	end_node(out_file)
	end_children(out_file)

	# finish	
	end_root(out_file)
	end_map(out_file, "sheet 1")
	
	out_file.close()


###############################################################################


