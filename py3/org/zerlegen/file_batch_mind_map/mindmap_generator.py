#!/usr/bin/python3

################################################################################
# Simple script that reads a batch of files and dumps them into a mind map as
# attachments.  Each file has a child node descending from the root node.
################################################################################

import os
import re
import sys
import shutil

import org.zerlegen.pyXmind.xmind_utils as xmind_utils
import org.zerlegen.pyXmind.xmind_xml as xmind_xml
from org.zerlegen.pyXmind.xmind_manifest import XMindManifest as XManifest


ATT_DIR_NAME = "./attachments"

def add_file(fname, content_out, manifest):
    # generate unique id for file
    print(manifest)
    id = xmind_utils.generate_object_id()
    #
    print("generated id: " + id + " for file: " + fname)
    #
  
    # parse out file extension
    id_name = id
    if fname.__contains__('.'):
        fname_components = fname.split('.')
        ext = fname_components[len(fname_components) - 1]
        id_name = id + '.' + ext
        #
        print("id_name: " + id_name)
        #
    att_path = os.path.join(ATT_DIR_NAME, id_name)
   
    # copy file to attachments dir
    shutil.copyfile(fname, os.path.join(ATT_DIR_NAME, id_name))
    
    # add file to manifest
    manifest.add_file_entry("attachments/" + id_name, manifest.MEDIA_TYPE_NONE)

    print(manifest._file_entries)
    # add node for file to content.xml
    xmind_xml.begin_node(content_out, None, fname, id_name)
    xmind_xml.end_node(content_out)
    

################################################################################
# argv[1] - root directory to add files from
# argv[2] - regex matching filenames to add
# argv[3[ - content.xml out file
# argv[4] - manifest.xml out file


if __name__ == "__main__":
    root_dir = sys.argv[1]
    file_pat = re.compile(sys.argv[2])
    content_out = open(sys.argv[3], "w")
    manifest_out = sys.argv[4]

    # output dir for attachment files
    if not os.path.exists(ATT_DIR_NAME):
        os.makedirs(ATT_DIR_NAME)

    manifest = XManifest()

    manifest.add_file_entry("attachments/", manifest.MEDIA_TYPE_NONE)
    print(manifest._file_entries)

    #begin mind map
    xmind_xml.begin_map(content_out, xmind_xml.XMIND_THEME_SIMPLE)
    xmind_xml.begin_root(content_out, xmind_xml.XMIND_STRUCT_LOGIC_RIGHT,
                         root_dir)
    xmind_xml.begin_children(content_out)

    for (dir, subs, files) in os.walk(root_dir):
        for file in files:
            if file_pat.match(file):
                add_file(os.path.join(dir, file), content_out, manifest) 

    # add "hard" manifest entries
    manifest.add_file_entry("content.xml", manifest.MEDIA_TYPE_TEXT_XML)
    manifest.add_file_entry("META-INF/", manifest.MEDIA_TYPE_NONE)
    manifest.add_file_entry("META-INF/manifest.xml", manifest.MEDIA_TYPE_TEXT_XML)
    manifest.add_file_entry("meta.xml", manifest.MEDIA_TYPE_TEXT_XML)
    
    print(manifest._file_entries)
    manifest.write_manifest_file(manifest_out)    
       
    xmind_xml.end_children(content_out) 
    xmind_xml.end_root(content_out)
    xmind_xml.end_map(content_out, "sheet1")

   
