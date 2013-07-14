#!/usr/bin/python3

################################################################################
# Representation of a type hierarchy.  Given a root directory of a source file 
# tree, files are parsed to determine class and parent class names. The class 
# names are then populated into a series of trees based on class inheritence.
# 
# The root node of each tree has either a top-level class or a class that 
# from a 3rd party library. Subclasses in the source tree are then added as 
# child nodes.
#
# Each tree can then be traversed in a depth-first fashion.  
#
# To save space, only one copy of the class name is stored in the master type
# list "_type_list".  Hashes of the class name are then used elsewhere to track 
# relationships with other classes.
# 
################################################################################

import os
import re

class TypeHierarchy:
  
    _type_list = {}
    _roots = []
    _current_node = None
    _dependencies = []
        
 
    ####################################################################
    # Initially populates the type hierarchy tree
    #
    # src_root - Root directory of source files
    # dep_root - Root directory of external dependencies for source
    #
    # This is left as a stub to be implemented by language-specific
    # subclasses
    #
    #
    
    def __init__(self, src_root, dep_root):
        pass
                    
    ####################################################################
    # Return an iterator over this type hierarchy
    #
    #

    def __iter__(self):
       return self


    ####################################################################
    # Return the root nodes of this hierarchy.  These are the starting
    # point in each hierarchy tree representing either a top level type
    # in the source tree, or from an external library
    #
    #

    def get_root_nodes(self):
        return self._roots


    ####################################################################
    # Return the name of a type corresponding to a given hash stored in
    # the hierarchy
    #
    # node_id - hash of the type whose name to return
    # RETURN - the name of the type
    #
    #


    def get_node_name(self, node_id):
        #
        #print("node_id: " + str(node_id))
        #
        (name, children) = self._type_list[node_id] 
        return name

    
    ####################################################################
    # Return a list of child types for a given type.  The list contain
    # hashes of the type names.  The full type names can be retrieved
    # by calling get_node_name()
    #
    # node_id - the type whose children to return
    # RETURN - a list of hashes corresponding to the child types for
    # the type identified by "node_id"
    #
    #

    def get_children(self, node_id):
        (name, children) = self._type_list[node_id] 
        return children


    ####################################################################
    # Add a type name from an external library.  If types in our source
    # tree descend from this type, it will be added as a root node in
    # the hierarchy
    #
    #

    def _add_dependency(self, type_name):
        self._dependencies.append(hash(type_name))
    

    ####################################################################
    # Adds a type name to the hierarchy.  Does not add the type if the
    # hash of this type already exists in the hierarchy.
    # 
    # name - name of the type to add
    # parents - list of parent class(es) this type descends from
    #
    #

    def _add_type(self, type_name, parents):

        #
        #print("len parents: " + str(len(parents)))
        #
        def _assign_type(id, name, children):
            #
            #print("adding type: " + name)
            #
            self._type_list[id] = (name, children)

        # Add type if not already existing 
        name_id = hash(type_name)
            

        if (name_id in self._type_list) == False:
            _assign_type(name_id, type_name, [])
            if len(parents) == 0:
                #
                #print("adding root: " + type_name)
                #    
                self._roots.append(name_id)

        for parent in parents:
            parent_id = hash(parent)
            # Add parent if not already existing,
            # then add type as child of this parent
            if (parent_id in self._type_list) == False:
                _assign_type(parent_id, parent, [name_id])
                if (parent_id in self._dependencies):
                #
                #    print("adding root: " + parent)
                #
                    self._roots.append(parent_id)
            else:
                (pname, pchildren) = self._type_list[parent_id]
                pchildren.append(name_id)
                _assign_type(parent_id, pname, pchildren)
    
 
    ####################################################################
    # Print out the master type list and root nodes for this directory
    # (for debugging)
    #
    #

    def _print(self):
        print(self._type_list)
        print(self._roots)
        

    ####################################################################
    # BEGIN UNIT TESTS
    ####################################################################

    ####################################################################
    # Basic unit test to verify tree mechanics
    #
    def _hierarchy_test1(self):
        test_hier = TypeHierarchy('', '')
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

        def traverse(hier, node_id):
            print(str(hier.get_node_name(node_id)))
            children = hier.get_children(node_id)
            for child in children:
                traverse(hier, hash(child))

        for root_id in test_hier.get_root_nodes():
            traverse(test_hier, root_id)
            
    ####################################################################
    # END UNIT TESTS
    ####################################################################
 
        
