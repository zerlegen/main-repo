#!python3

import os
import stat

class command_mappings:

################################################################################ 

  _aliases = []
  #_tag_lists
  _cmd_strs = []

  def add_mapping(self, cmd, alias, tag_list):
    self._cmd_strs.append(cmd)
    #self._tag_lists.append(tag_list)
    self._aliases.append(alias)
    #print(self._cmd_strs)
    #print(self._aliases)

  def generate_shortcuts(self): 
    for i in range(len(self._cmd_strs)):
      cmd = self._cmd_strs[i]
      alias = self._aliases[i]
      out_path = "./shortcuts/" + alias + ".py"
      with open(out_path, "w") as out_file:
        out_file.write("#!python3\n")
        out_file.write("\n")
        out_file.write("import cmd_utils\n")
        out_file.write("import sys\n")
        out_file.write("\n")
        out_file.write("eval(\"" + "cmd_utils." + cmd + "\")") 
      os.chmod(out_path, stat.S_IRWXU)

################################################################################

def add_bash_mapping(line, map_obj):
  tokens = line.split()
  alias = tokens[1]
  in_list = tokens[2:]
  in_str = "print_command_output(["
  for i in range(len(in_list)):
    if (in_list[i]).startswith("sys.argv"): 
      in_str += in_list[i] 
    else:
      in_str += "\'" + in_list[i] + "\'"
    if (i + 1) < len(in_list):
      in_str += ", "
  in_str += "])"
  print(in_str)
  map_obj.add_mapping(in_str, alias, [])
 


################################################################################

if __name__ == "__main__":

  map1 = command_mappings()

  # load bash command mappings
  with open("commands.txt", "r") as in_file:
    for line in in_file.readlines():
      if line.startswith("bash"):
        add_bash_mapping(line, map1) 
      elif line.startswith("#"):
        continue
                         

  map1.generate_shortcuts()
