#!python3

class command_mappings:
  
  _aliases
  #_tag_lists
  _cmd_strs

  def add_mapping(self, cmd, alias, tag_list):
    self._cmd_strs.append(cmd)
    #self._tag_lists.append(tag_list)
    self._aliases.append(alias)

  def generate_shortcuts(self): 
    for i in range(len(_cmd_strs)):
      cmd = self._cmd_strs[i]
      alias = self._aliases[i]
      with open("shortcuts/" + alias + ".py", "w") as out_file:
        out_file.write("#!python3\n")
        out_file.write("\n")
        out_file.write("import cmd_utils\n")
        out_file.write("\n")
        out_file.write("eval(\"" + cmd + "\")") 
