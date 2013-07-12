#!/usr/bin/python3

import re
import os
import zipfile
import org.zerlegen.source_analyzer.type_hierarchy as type_hierarchy
from type_hierarchy import TypeHierarchy as TypeHierarchy
import org.zerlegen.source_analyzer.java_analyzer

import pdb

class JavaTypeHierarchy (TypeHierarchy):

    _dependencies = []

    def _load_jar_file(self, file):
#        #class_name_patn = re.compile(
        zf = zipfile.ZipFile(file, 'r')
        try:
            flist = zf.infolist()
            for entry in flist:
                fname = entry.filename
                if fname.endswith('.class'):
                    print('loading class file: ' + fname)
        finally:
            zf.close()

                    

    ########################################################################### 
    # Loads type names from dependency jars in root_dir.  Dependency types that
    # types in our source tree descend from will be treated as roots in our
    # hierarchy.
    #
    def _load_dependency_types(self, root_dir):
        for (dir, subs, files) in os.walk(root_dir):
            for file in files:
                print("checking dep file: " + file)
                if file.endswith('.jar'):
                    self._load_jar_file(os.path.join(dir, file))


    def _parse_java_file(self, filename):
        type_pat = re.compile(".*class (.+) ?")
        parent_pat = re.compile(".+ extends (.+) ?")

        type_name = ""
        parent_name = ""

        fh = open(filename, 'r')
        lines = fh.readlines()
        for line in lines:
            type_match = type_pat.search(line)
            parent_match = parent_pat.search(line)

            if type_match != None:
                type_name = type_match.group(1)
                #print("parsed type name: " + type_name)
            if parent_match != None:
                parent_name = parent_match.group(1)
                #print("parsed parent name: " + parent_name)

        return (type_name, parent_name)


    ########################################################################### 
    # src_root - source tree root directory
    # dep_root - dependency root directory
    #

    def __init__(self, src_root, dep_root):
        self._load_dependency_types(dep_root)

        for (dir, subs, files) in os.walk(src_root):
            for file in files:
                if file.endswith('.java'):
                    print("Adding file: " + os.path.join(dir, file))
                    full_path = os.path.join(dir, file)
                    (type_name, parent_name) = self._parse_java_file(full_path) 
                    print("got type: " + type_name)
                    print("got parent: " + parent_name)
                    if parent_name == "" or len(parent_name) == 0:
                        self._add_type(type_name, [])
                    else:
                        self._add_type(type_name, [parent_name])
                    #self._print()
                    
        
            
        #pdb.set_trace()
#        self._add_type('', ['parent'])
#        self._print()
#        print('-------------')
#        self._add_type('grandparent', []) 
#        self._print()
#        print('-------------')
#        self._add_type('parent', ['grandparent'])
#        self._print()
#        print('-------------')
#        self._add_type('grandchild', ['child'])
#        self._print()
#        print('-------------')
#        self._add_type('child', ['base'])
#        self._print()

    #def test():
#test_hier = JavaTypeHierarchy('/home/epom/test-repo/portecle/src/main', '^\S+\.java')
#test_hier._add_type('one', []) 
#test_hier._add_type('two', ['one'])
#
#test_hier._add_type('five', ['one'])
#test_hier._add_type('six', ['one'])
#
#test_hier._add_type('three', ['two'])
#
#test_hier._add_type('four', ['two'])  
#
#test_hier._add_type('seven', [])
#test_hier._add_type('eight', ['seven'])
#test_hier._add_type('nine', ['seven'])
#test_hier._add_type('ten', ['seven'])
#test_hier._add_type('eleven', ['ten'])
#test_hier._add_type('twelve', ['eleven'])
#test_hier._add_type('thirteen', ['eleven'])
#test_hier._add_type('fourteen', ['thirteen'])


#pdb.set_trace() 
#while True:
#    try:
#        print(test_hier.next())
#    except StopIteration:
#        print("end of iteration")
#        break
#test_hier._print() 
   
