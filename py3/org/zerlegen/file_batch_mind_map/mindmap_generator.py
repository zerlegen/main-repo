#!/usr/bin/python3

################################################################################
# Simple script that reads a batch of files and dumps them into a mind map as
# attachments.  Each file has a child node descending from the root node.
################################################################################

import os
import re

import org.zerlegen.pyXmind.xmind_xml
from org.zerlegen.pyXmind.xmind_manifest import XMindManifest as XManifest

def add_file(fname, manifest):
    # generate unique id for file
    # add file to manifest
    # add node for file to content.xml
    pass

################################################################################
# argv[1] - root directory to add files from
# argv[2] - regex matching filenames to add
# argv[3[ - content.xml out file
# argv[4] - manifest.xml out file


if __name__ == "__main__":
    root_dir = sys.argv[1]
    file_pat = re.compile(sys.argv[2])
    out_content_xml = open(sys.argv[3])
    out_manifest_xml = open(sys.argv[4])

    manifest = XManifest()


    for (dir, subs, files) in os.walk(root_dir):
        for file in files:
            if file_pat.match(file):
                add_file(file, manifest)     
       
        
        
