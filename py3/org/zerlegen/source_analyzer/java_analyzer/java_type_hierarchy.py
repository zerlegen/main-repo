#!/usr/bin/python3

import re
import os
import zipfile
import org.zerlegen.source_analyzer.type_hierarchy as type_hierarchy
from type_hierarchy import TypeHierarchy as TypeHierarchy
import org.zerlegen.source_analyzer.java_analyzer

################################################################################
# Subclass of TypeHierarchy that implements a type hierarchy for java
#
# Loads dependencies from external jar files and considers these "root" types
# in the generated mindmap.  .java files in the specified source tree are 
# parsed for class declarations.  We assume for now that a buffer of 5 lines
# will 1) completely enclose a class declaration, and 2) contain only one
# declaration
#
#

class JavaTypeHierarchy (TypeHierarchy):

    _dependencies = []


    ########################################################################### 
    # Load dependencies from a jar file
    #
    # jar_file - the jar to load types from
    # return - nothing
    #

    def _load_jar_file(self, jar_file):
        print("loading jar file: " + jar_file)
        class_name_patn = re.compile("/([^\s/]+).class$")
        zf = zipfile.ZipFile(jar_file, 'r')
        try:
            flist = zf.infolist()
            for entry in flist:
                fname = entry.filename
                if fname.endswith('.class'):
                    #
                    print('loading class file: ' + fname)
                    #
                    searchobj = class_name_patn.search(fname)
                    if (searchobj != None):
                        class_name = searchobj.group(1)
                        self._add_dependency(class_name)
                    #
                    #print("class name: " + class_name)
                    #
        finally:
            #
            #print("_dependencies: " + str(self._dependencies))
            #
            zf.close()

                    

    ########################################################################### 
    # Loads type names from dependency jars in root_dir.  Dependency types that
    # types in our source tree descend from will be treated as roots in our
    # hierarchy.
    #
    # root_dir - root directory to search for jar files
    # return - nothing
    #

    def _load_dependency_types(self, root_dir):
        for (dir, subs, files) in os.walk(root_dir):
            for file in files:
            #
            #    print("checking dep file: " + file)
            #
                if file.endswith('.jar'):
                    self._load_jar_file(os.path.join(dir, file))

    ################################################################################ 
    # Parses a java file for class declarations
    #
    # file_name - name of the java file
    # return - a list of pairs consisting of the class name and parent name 
    # (if there is one)
    # for this java file
    #
    #
    
    def _parse_java_file(self, file_name):
        #
        #print("parsing file: " + file_name)
        #
        fh = open(file_name, "r")
        found = []
      
        open_brace = re.compile(".*{")
        class_pat = re.compile(".*class\s+(\w+).*\{")
        parent_pat = re.compile(".*extends\s+(\w+)(\s+)?\{?")
 
        # scan a buffer of 5 lines for a class declaration
        # we assume a class declaration (from "class" to "{")
        # won't be more than 5 lines, and that there will only
        # be one declaration per 5 lines 
        line_i = fh.readline().rstrip()
        line_j = fh.readline().rstrip()
        line_k = fh.readline().rstrip()
        line_l = fh.readline().rstrip()
        line_m = fh.readline().rstrip()

        while (True):

            type_name = None
            parent_name = None 

            buf = line_i + line_j + line_k + line_l + line_m
            #
            #print("buf: " + buf)
            #
         
            if not buf:
                # we've reached the end of the file 
                break
        
                    
            if open_brace.match(buf):
                if class_pat.match(buf):
                    type_name = class_pat.search(buf).group(1)
                    #
                    print("found class: " + type_name)
                    #
                    if parent_pat.match(buf):
                        parent_name = parent_pat.search(buf).group(1)
                        #
                        print("found parent: " + parent_name)
                        #
                    if parent_name == None:
                        found.append((type_name, None))
                    else:
                        found.append((type_name, parent_name))

                    #we found a class declaration, advance 5 lines
                    line_i = fh.readline().rstrip()
                    line_j = fh.readline().rstrip()
                    line_k = fh.readline().rstrip()
                    line_l = fh.readline().rstrip()
                    line_m = fh.readline().rstrip()
                    
                    continue
            
            # advance buffer by one line
            line_i = line_j
            line_j = line_k
            line_k = line_l
            line_l = line_m
            line_m = fh.readline().rstrip()    

        return found


    ########################################################################### 
    # src_root - source tree root directory
    # dep_root - dependency root directory
    #

    def __init__(self, src_root, dep_root):
        self._load_dependency_types(dep_root)

        for (dir, subs, files) in os.walk(src_root):
            for file in files:
                if file.endswith('.java'):
                    #
                    #print("Adding file: " + os.path.join(dir, file))
                    #
                    full_path = os.path.join(dir, file)
                    found = self._parse_java_file(full_path)
                    if found == []:
                        # no classes in this file, skip for now
                        continue
                                        #
                    else:
                        for (type_name, parent_name) in found:
                            #print("got type: " + type_name)
                            #print("got parent: " + str(parent_name))

                            if parent_name == None:
                                self._add_type(type_name, [])
                            else:
                                self._add_type(type_name, [parent_name])
                    #self._print()

        print("added " + str(len(self._type_list)) + " types")
        

                        
  
