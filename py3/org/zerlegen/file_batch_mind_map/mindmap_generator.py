#!/usr/bin/python3

################################################################################
# Simple script that reads a batch of files and dumps them into a mind map as
# attachments.  Each file has a child node descending from the root node.
################################################################################

import os
import re
import sys
import shutil
import tempfile

import org.zerlegen.pyXmind.xmind_mindmap_builder as xmind_mindmap_builder


################################################################################
# argv[1] - root directory to add files from
# argv[2] - regex matching filenames to add
# argv[3[ - output mindmap file


if __name__ == "__main__":
    root_dir = sys.argv[1]
    file_pat = re.compile(sys.argv[2])
    wrkbk_out = sys.argv[3]

    meta_path = "/home/epom/test-repo/py3/org/zerlegen/pyXmind/test-in/meta.xml"
    builder = xmind_mindmap_builder.XMindMindmapBuilder(root_dir, 
      "org.xmind.ui.logic.right", meta_path)
    builder.begin_children()

    for (dir, subs, files) in os.walk(root_dir):
        for file in files:
            if file_pat.match(file):
                path = os.path.join(dir, file)
                builder.begin_node("org.xmind.ui.map.logic.right", file, os.path.join(dir, file))
                builder.end_node()

    builder.end_children()
    builder.close_map()
    builder.build_workbook(wrkbk_out)    


    

   
