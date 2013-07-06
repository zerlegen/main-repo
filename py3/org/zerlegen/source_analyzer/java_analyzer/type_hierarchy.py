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
    def __iter__(self):
       return self


    ####################################################################
    def _visit(self):

#        if(self._current_node != None):
#            (name, children) = self._type_list[self._current_node]
#            print("current node: " + str(name))
#        else:
#            print("current node: none")
#        print("stack: " + str(self._traverse_stack))


        if self._current_node == None:
            if len(self._roots) == 0:
                # We've traversed all trees
                raise StopIteration
            else:
                # Start a new tree
                self._current_node = self._roots.pop()
                (name, children) = self._type_list[self._current_node]
                return name
        else:
            (name, children) = self._type_list[self._current_node]
            if len(children) > 0:
                child = children.pop()
                self._traverse_stack.insert(0, self._current_node)
                self._current_node = hash(child)
                (name, children) = self._type_list[self._current_node]
                return name
            else:
                while self._current_node != None:
                    if len(self._traverse_stack) > 0:
                        self._current_node = self._traverse_stack.pop(0)
                        (name, children) = self._type_list[self._current_node]
                        if len(children) > 0:
                            child = children.pop()
                            self._traverse_stack.insert(0, self._current_node)
                            self._current_node = hash(child)
                            (name, children) = self._type_list[self._current_node]
                            return name
                        else:
                            continue
                    else: 
                        self._current_node = None
                return self._visit()


    ####################################################################
    def next(self):
        return self._visit() 
        
    
    ####################################################################
    # Adds a type name to the hierarchy.
    # 
    # name - name of the type to add
    # parents - list of parent class(es) this type descends from

    def _add_type(self, type_name, parents):

        # Add type if not already existing 
        name_id = hash(type_name)

        if (name_id in self._type_list) == False:
            self._type_list[name_id] = (type_name, [])
            if len(parents) == 0:
                self._roots.append(name_id)

        for parent in parents:
            parent_id = hash(parent)
            # Add parent if not already existing,
            # then add type as child of this parent
            if (parent_id in self._type_list) == False:
                self._type_list[parent_id] = (parent, [type_name])
            else:
                (pname, pchildren) = self._type_list[parent_id]
                pchildren.append(type_name)
                self._type_list[parent_id] = (pname, pchildren) 
         
  
    def _print(self):
        print(self._type_list)
        print(self._roots)
        

    def next(self):
        pass       
 
    def root(self):
        pass

    def children_of(self, parent):
        pass

    def add_file(self, filename):
        raise NotImplemented ("Implemented by language-specific subclass!")



      
        
