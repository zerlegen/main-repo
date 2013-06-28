#!/usr/bin/python3

import time
import sys

###############################################################
# define templates for content.xml in Xmind workbooks



XMIND_CHILDREN_OPEN = """<children>"""
XMIND_CHILDREN_CLOSE = """</children>"""
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

def write_XMIND_TOPIC_OPEN(outFile, timestamp):
	outFile.write("<topic id=\"5jlu3jotvfr94mnaran8caioqv\"" + 
		      " structure-class=\"org.xmind.ui.map.clockwise\" timestamp=\"" + 
                      timestamp + "\">")

def write_XMIND_TOPIC_CLOSE(outFile):
	outFile.write("</topic>")

def write_XMIND_CHILDREN_OPEN(outFile):
	outFile.write("<children>")

def write_XMIND_CHILDREN_CLOSE(outFile):
	outFile.write("</children>")


def generate_xmind_timestamp():
	return (str(int(time.time()) * 1000))

##################################################################


outFileName = "test-out.xml"
#outFile = open(outFileName, 'w')
outFile = sys.stdout

write_XMIND_HEADER(outFile)
write_XMIND_XMAP_CONTENT_OPEN(outFile, generate_xmind_timestamp())
write_XMIND_SHEET_OPEN(outFile, "brainy.defaultGenre.simple",
		       generate_xmind_timestamp())
 
write_XMIND_TOPIC_OPEN(outFile, generate_xmind_timestamp())
write_XMIND_TITLE(outFile, "root")
write_XMIND_CHILDREN_OPEN(outFile)

write_XMIND_TOPICS_OPEN(outFile)

write_XMIND_TOPIC_OPEN(outFile, generate_xmind_timestamp())
write_XMIND_TITLE(outFile, "child")
write_XMIND_TOPIC_CLOSE(outFile)

write_XMIND_TOPIC_OPEN(outFile, generate_xmind_timestamp())
write_XMIND_TITLE(outFile, "child2")

write_XMIND_CHILDREN_OPEN(outFile)
write_XMIND_TOPICS_OPEN(outFile)
write_XMIND_TOPIC_OPEN(outFile, generate_xmind_timestamp())
write_XMIND_TITLE(outFile, "grandchild")
write_XMIND_TOPIC_CLOSE(outFile)
write_XMIND_TOPICS_CLOSE(outFile)
write_XMIND_CHILDREN_CLOSE(outFile)

write_XMIND_TOPIC_CLOSE(outFile)



write_XMIND_TOPICS_CLOSE(outFile)

write_XMIND_CHILDREN_CLOSE(outFile)
write_XMIND_TOPIC_CLOSE(outFile)

write_XMIND_TITLE(outFile, "Sheet 1")
write_XMIND_SHEET_CLOSE(outFile)
write_XMIND_XMAP_CONTENT_CLOSE(outFile)

outFile.close()



