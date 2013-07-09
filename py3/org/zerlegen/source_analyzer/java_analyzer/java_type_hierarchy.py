#!/usr/bin/python3


import org.zerlegen.source_analyzer.type_hierarchy as type_hierarchy
from type_hierarchy import TypeHierarchy as TypeHierarchy

import org.zerlegen.source_analyzer.java_analyzer

#import org.zerlegen.source_analyzer.type_hierarchy.TypeHierarchy
import pdb

class JavaTypeHierarchy (TypeHierarchy):

    def add_file(self, filename):
       pass

    def __init__(self, root_dir, file_filter):
       pass
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
test_hier = JavaTypeHierarchy('/home/epom/test-repo/portecle/src/main', '^\S+\.java')
test_hier._add_type('one', []) 
test_hier._add_type('two', ['one'])

test_hier._add_type('five', ['one'])
test_hier._add_type('six', ['one'])

test_hier._add_type('three', ['two'])

test_hier._add_type('four', ['two'])  

test_hier._add_type('seven', [])
test_hier._add_type('eight', ['seven'])
test_hier._add_type('nine', ['seven'])
test_hier._add_type('ten', ['seven'])
test_hier._add_type('eleven', ['ten'])
test_hier._add_type('twelve', ['eleven'])
test_hier._add_type('thirteen', ['eleven'])
test_hier._add_type('fourteen', ['thirteen'])


#pdb.set_trace() 
#while True:
#    try:
#        print(test_hier.next())
#    except StopIteration:
#        print("end of iteration")
#        break
#test_hier._print() 
   
