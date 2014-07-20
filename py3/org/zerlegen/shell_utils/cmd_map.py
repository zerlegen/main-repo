#!python3

class command_mappings:
  
  _aliases = []
  #_tag_lists
  _cmd_strs = []

  def add_mapping(self, cmd, alias, tag_list):
    self._cmd_strs.append(cmd)
    #self._tag_lists.append(tag_list)
    self._aliases.append(alias)
    print(self._cmd_strs)
    print(self._aliases)

  def generate_shortcuts(self): 
    for i in range(len(self._cmd_strs)):
      cmd = self._cmd_strs[i]
      alias = self._aliases[i]
      with open("./shortcuts/" + alias + ".py", "w") as out_file:
        out_file.write("#!python3\n")
        out_file.write("\n")
        out_file.write("import cmd_utils\n")
        out_file.write("\n")
        out_file.write("eval(\"" + "cmd_utils." + cmd + "\")") 

if __name__ == "__main__":

  map1 = command_mappings()

  # load bash command mappings
  with open("commands.txt", "r") as in_file:
    for line in in_file.readlines():
      if line.startswith("bash"):
        tokens = line.split()
        alias = tokens[1]
        in_list = tokens[2:]
        in_str = "print_command_output(["
        for i in range(len(in_list)):
          in_str += "\'" + in_list[i] + "\'"
          if (i + 1) < len(in_list):
            in_str += ", "
        in_str += "])"
        #print(in_str)
        map1.add_mapping(in_str, alias, [])
        
                         

  map1.generate_shortcuts()
