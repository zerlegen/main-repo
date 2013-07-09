#!/usr/bin/python3

################################################################################
# Representation of a type hierarchy.  Given a source tree, files are
# parsed to determine class and parent class names.  The class names are then
# populated into a series of trees. 
#
# The root node of each tree has either a top-level class or a class that 
# descends from a 3rd party library. Subclasses are then added as child nodes.
#
# Each tree can then be traversed in a depth-first fashion.  

################################################################################

import os
import re

class TypeHierarchy:
  
    _type_list = {}
    _roots = []
    _traversing = 0
    _traverse_stack = []
    _current_node = None
        
 
    ####################################################################
    # Initially populates the type hierarchy tree
    #
    # root_dir - Root directory of source files
    # file_filter - regex specifying source files to include 
    #
    
    def __init__(self, root_dir, file_filter):
        pattern = re.compile(file_filter)
        for (current, subs, files) in os.walk(root_dir):
            for file in files:
                if re.search(pattern, file) != None:
                    #print('matched: ' + file)
                    self.add_file(file)

                    
    ####################################################################
    #

    def __iter__(self):
       return self


    def get_root_nodes(self):
        return self._roots

    def get_node_name(self, node_id):
        (name, children) = self._type_list[node_id] 
        return name

    def get_child_nodes(self, node_id):
        (name, children) = self._type_list[node_id] 
        return children

    
    ####################################################################
    # Traverses the type hierarchy.  On each call, returns a pair
    # consisting of the current type, and an integer indicating the 
    # depth change from the last returned type.
    #
    # Possible values for depth change:
    #
    # None - the returned type is a new root in a new hierarchy
    # +1 - the returned type is a child of the previously returned type.
    #      Intuitively, "depth increases by 1"
    # -X - the returned type is a child of an ancestor of the previously 
    #  returned type.  X indicates the number of steps up the hierarchy 
    #  to the ANCESTOR.  For example, -2 indicates the returned type is 
    #  a child of the previous type's grandparent
    
    def next(self):

        def push(type):
            self._traverse_stack.insert(0, type)

        def pop():
            return self._traverse_stack.pop(0)

        def get_current_name():
            (name, children) = self._type_list[self._current_node]
            return name

        def get_current_children():
            (name, children) = self._type_list[self._current_node]
            return children

        if self._current_node == None:
            if len(self._roots) == 0:
                # We've traversed all trees
                raise StopIteration
            else:
                # Start a new tree
                self._current_node = self._roots.pop()
                return (get_current_name(), None)
        else:
            children = get_current_children()
            if len(children) > 0:
                previous = get_current_name()
                child = children.pop()
                push(self._current_node)
                self._current_node = hash(child)
                return (get_current_name(), 1)
            else:
                depth_change = 0
                while self._current_node != None:
                    if len(self._traverse_stack) > 0:
                        self._current_node = pop()
                        depth_change += -1
                        children = get_current_children()
                        if len(children) > 0:
                            previous = get_current_name()
                            child = children.pop()
                            push(self._current_node)
                            self._current_node = hash(child)
                            return (get_current_name(), depth_change)
                        else:
                            # no more children for this parent, 
                            # keep going up
                            continue
                    else:
                        #we've reached the top of this tree 
                        self._current_node = None
                return self.next()
   
 
    ####################################################################
    # Adds a type name to the hierarchy.
    # 
    # name - name of the type to add
    # parents - list of parent class(es) this type descends from

    def _add_type(self, type_name, parents):

        def _add_type_name(id, name, children):
            self._type_list[id] = (name, children)

        # Add type if not already existing 
        name_id = hash(type_name)

        if (name_id in self._type_list) == False:
            _add_type_name(name_id, type_name, [])
            if len(parents) == 0:
                self._roots.append(name_id)

        for parent in parents:
            parent_id = hash(parent)
            # Add parent if not already existing,
            # then add type as child of this parent
            if (parent_id in self._type_list) == False:
                _add_type_name(parent_id, parent, [type_name])
            else:
                (pname, pchildren) = self._type_list[parent_id]
                pchildren.append(name_id)
                _add_type_name(parent_id, pname, pchildren)
         
 
 
    ####################################################################
    #

    def _print(self):
        print(self._type_list)
        print(self._roots)
        

    ####################################################################
    #

    def add_file(self, filename):
        raise NotImplemented ("Implemented by language-specific subclass!")



      
        
