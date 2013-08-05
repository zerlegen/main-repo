#!/usr/bin/python3

###############################################################################
# Generates XML for an XMind mind map tree in a depth-first fashion.
# The XML is written to "content.xml", which then must be assembled
# as part of an XMind workbook.  A workbook is a zip file that internally
# contains XML content, style metadata etc...
# 
###############################################################################

import sys
import org.zerlegen.pyXmind.xmind_utils as xmind_utils

###############################################################################
# low level write functions - write XML for each field to the passed output
# file
###############################################################################

XMIND_STRUCT_LOGIC_RIGHT = "org.xmind.ui.logic.right"
XMIND_STRUCT_MAP_CLOCKWISE = "org.xmind.ui.map.clockwise"
XMIND_THEME_SIMPLE = "brainy.defaultGenre.simple"


def _write_XMIND_HEADER(out_file, encoding="UTF-8"):
	out_file.write("<?xml version=\"1.0\" encoding=\"" + encoding + 
		      "\"" + " standalone=\"no\"?>")
		     
def _write_XMIND_TITLE(out_file,  text):
	out_file.write("<title>" + text + "</title>")

def _write_XMIND_XMAP_CONTENT_OPEN(out_file, timestamp):
	out_file.write(
	"<xmap-content xmlns=\"urn:xmind:xmap:xmlns:content:2.0\" " +
	"xmlns:fo=\"http://www.w3.org/1999/XSL/Format\" " + 
	"xmlns:svg=\"http://www.w3.org/2000/svg\" " +
	"xmlns:xhtml=\"http://www.w3.org/1999/xhtml\" " + 
	"xmlns:xlink=\"http://www.w3.org/1999/xlink\" " +
	"timestamp=\"" + timestamp + "\" version=\"2.0\">")

def _write_XMIND_XMAP_CONTENT_CLOSE(out_file):
	out_file.write("</xmap-content>")

def _write_XMIND_SHEET_OPEN(out_file, theme, timestamp, sheet_id):
	out_file.write("<sheet id=\"" + sheet_id + "\" theme=\"" + 
			theme + "\" timestamp=\"" + timestamp + "\">")

def _write_XMIND_SHEET_CLOSE(out_file):
	out_file.write("</sheet>")

def _write_XMIND_TOPICS_OPEN(out_file):
	out_file.write("<topics type=\"attached\">")

def _write_XMIND_TOPICS_CLOSE(out_file):
	out_file.write("</topics>")


###############################################################################
# Begin an XMind TOPIC XML object
#
# out_file: the output XML file
# structure: string constant defining structure of the new node
# timestamp: time stamp of the topic's creation
# topic_id: unique 13 byte ID hex string identifying the topic
# xlink_href: reference to an attachment for this topic, if there is one
###############################################################################

def _write_XMIND_TOPIC_OPEN(out_file, structure, timestamp, topic_id, xlink_href):
    
    xml_str = "<topic id=\"" + topic_id + "\"" 

    if structure != None:
        xml_str +=  " structure-class=\"" + structure + "\""   

    xml_str += " timestamp=\"" + timestamp + "\""

    if xlink_href != None:
        xml_str += " xlink:href=\"xap:attachments/" + xlink_href + "\""

    xml_str += ">"
    out_file.write(xml_str)


def _write_XMIND_TOPIC_CLOSE(out_file):
	out_file.write("</topic>")

def _write_XMIND_CHILDREN_OPEN(out_file):
	out_file.write("<children>")

def _write_XMIND_CHILDREN_CLOSE(out_file):
	out_file.write("</children>")


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
	_write_XMIND_HEADER(out_file)
	_write_XMIND_XMAP_CONTENT_OPEN(out_file, xmind_utils.generate_xmind_timestamp())
	_write_XMIND_SHEET_OPEN(out_file, theme, xmind_utils.generate_xmind_timestamp(),
                            xmind_utils.generate_object_id())

def begin_root(out_file, structure, title):
	_write_XMIND_TOPIC_OPEN(out_file, structure, xmind_utils.generate_xmind_timestamp(),
                            xmind_utils.generate_object_id(), None)
	_write_XMIND_TITLE(out_file, title)

def end_root(out_file):
	_write_XMIND_TOPIC_CLOSE(out_file)

def begin_children(out_file):
	_write_XMIND_CHILDREN_OPEN(out_file)
	_write_XMIND_TOPICS_OPEN(out_file)

def end_children(out_file):
	_write_XMIND_TOPICS_CLOSE(out_file)
	_write_XMIND_CHILDREN_CLOSE(out_file)


def begin_node(out_file, structure, title, attachment_fn=None):
	_write_XMIND_TOPIC_OPEN(out_file, structure, xmind_utils.generate_xmind_timestamp(),
                            xmind_utils.generate_object_id(), attachment_fn)
	_write_XMIND_TITLE(out_file, title)


def end_node(out_file):
	_write_XMIND_TOPIC_CLOSE(out_file)


def end_map(out_file, sheet_name):
	_write_XMIND_TITLE(out_file, sheet_name)
	_write_XMIND_SHEET_CLOSE(out_file)
	_write_XMIND_XMAP_CONTENT_CLOSE(out_file)
	out_file.close()

###############################################################################
# Unit Tests:
###############################################################################
#
# root -> child1 --> grandchild
#                --> grandchild2
#                --> grandchild3
#
#      --> child2 --> grandchild4
#

def test_two_children_four_grandchildren():

	out_file = sys.stdout
	begin_map(out_file, XMIND_THEME_SIMPLE)

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
def test_attachments():
    

    out_file = sys.stdout
    begin_map(out_file, XMIND_THEME_SIMPLE)
    
    # root node
    begin_root(out_file, XMIND_STRUCT_MAP_CLOCKWISE, "root node")
    begin_children(out_file)
    
    # first child	
    begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "child1", "Guido.jpg")

    #begin_node(out_file, XMIND_STRUCT_LOGIC_RIGHT, "child1")
    end_node(out_file)
    
    
    # finish	
    end_children(out_file)
    end_root(out_file)
    end_map(out_file, "sheet 1")
    
    out_file.close()




###############################################################################

if __name__ == "__main__":
    test_two_children_four_grandchildren()
    #test_attachments()

