#!/usr/bin/python3

import org.zerlegen.pyXmind.xmind_workbook_builder as xmind_workbook_builder
import org.zerlegen.pyXmind.xmind_utils as xmind_utils
import org.zerlegen.pyXmind.xmind_content as xmind_content
import tempfile
import os
import stat
import shutil

################################################################################
# Top level XMind mindmap API
################################################################################

class XMindMindmapBuilder:

    _in_content = None
    _builder = None
    _meta = ""

    def __init__(self, root_name, structure, meta_path):
        self._meta = meta_path
        self._builder = xmind_workbook_builder.XMindWorkbookBuilder()
        # open temp file for content.xml
        name = tempfile.mkstemp(suffix=".xml")[1]
        self._in_content = open(name, "w")
        xmind_content.begin_map(self._in_content, xmind_content.XMIND_THEME_SIMPLE)
        xmind_content.begin_root(self._in_content, 
                                 structure,
                                 root_name)

    def begin_children(self):
        xmind_content.begin_children(self._in_content)

    def end_children(self):
        xmind_content.end_children(self._in_content)
    
    def begin_node(self, structure, title, attachment_path=None): 
        id_name = None
        if attachment_path != None:
            id = xmind_utils.generate_object_id()
            self._builder.add_attachment(attachment_path, id)
            split = os.path.basename(attachment_path).split('.')
            if len(split) > 1:
                id_name = id + '.' + split[-1]
            else:
                id_name = id

        xmind_content.begin_node(self._in_content, structure, 
                                 title, id_name)
                
    def end_node(self):
        xmind_content.end_node(self._in_content)


    def close_map(self):
        xmind_content.end_root(self._in_content)
        xmind_content.end_map(self._in_content, "sheet 1")
        self._in_content.close()

    def build_workbook(self, out_file):
        self._builder.set_content_xml(self._in_content.name)
        #
        #shutil.copyfile(self._in_content.name, "./content2.xml")
        self._builder.set_meta_xml(self._meta)
        self._builder.build(out_file)

        # delete temp content xml
        os.remove(self._in_content.name)

################################################################################
# BEGIN UNIT TESTS
################################################################################

def testChild():
    meta_path = "/home/epom/test-repo/py3/org/zerlegen/pyXmind/test-in/meta.xml"
    mmBuilder = XMindMindmapBuilder("test_child", "org.xmind.ui.logic.right", meta_path)
    mmBuilder.begin_children()
    mmBuilder.begin_node("org.xmind.ui.map.clockwise", "child")
    mmBuilder.end_node()
    mmBuilder.end_children()
    mmBuilder.close_map()
    mmBuilder.build_workbook("test-child.xmind")

def testGrandChild():
    meta_path = "/home/epom/test-repo/py3/org/zerlegen/pyXmind/test-in/meta.xml"
    mmBuilder = XMindMindmapBuilder("test_grandchild", "org.xmind.ui.logic.right", meta_path)
    mmBuilder.begin_children()
    mmBuilder.begin_node("org.xmind.ui.map.clockwise", "child")
    mmBuilder.begin_children()
    mmBuilder.begin_node("org.xmind.ui.map.clockwise", "grandchild")
    mmBuilder.end_node()
    mmBuilder.end_children()
    mmBuilder.end_node()
    mmBuilder.end_children()
    mmBuilder.close_map()
    mmBuilder.build_workbook("test-grandchild.xmind")


def testAttachment():
    meta_path = "/home/epom/test-repo/py3/org/zerlegen/pyXmind/test-in/meta.xml"
    mmBuilder = XMindMindmapBuilder("test_attachment", "org.xmind.ui.logic.right", meta_path)
    mmBuilder.begin_children()
    mmBuilder.begin_node("org.xmind.ui.map.clockwise", "child",
                         os.path.join(os.getcwd(), "build", "Guido.jpg"))
    mmBuilder.begin_children()
    mmBuilder.begin_node("org.xmind.ui.map.clockwise", "child",
                         os.path.join(os.getcwd(), "build", "Guido.jpg"))
    mmBuilder.end_node()
    mmBuilder.end_children()
    mmBuilder.end_node()
    mmBuilder.end_children()
    mmBuilder.close_map()
    mmBuilder.build_workbook("test-attachment.xmind")


        

if (__name__ == "__main__"):
    testChild()
    testGrandChild()
    testAttachment()


