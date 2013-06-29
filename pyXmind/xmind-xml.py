#!/usr/bin/python3

import time
import sys


###############################################################


def write_XMIND_HEADER(outFile, encoding="UTF-8"):
	outFile.write("<?xml version=\"1.0\" encoding=\"" + encoding + "\" standalone=\"no\"?>")

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

##################################################################


XMIND_STRUCT_LOGIC_RIGHT = "org.xmind.ui.logic.right"
XMIND_STRUCT_MAP_CLOCKWISE = "org.xmind.ui.map.clockwise"



outFileName = "test-out.xml"

outFile = sys.stdout

begin_map(outFile, "brainy.defaultGenre.simple")

begin_root(outFile, XMIND_STRUCT_MAP_CLOCKWISE, "root node")

begin_children(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "child1")

begin_children(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild")

end_node(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild2")

end_node(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild3")

end_node(outFile)



end_children(outFile)

end_node(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "child2")


begin_children(outFile)

begin_node(outFile, XMIND_STRUCT_LOGIC_RIGHT, "grandchild4")

end_node(outFile)

end_children(outFile)

end_node(outFile)

end_children(outFile)

end_root(outFile)

end_map(outFile)

outFile.close()



