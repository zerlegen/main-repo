#!python3


import subprocess

def print_command_output(prog_args_list, run_in_shell=False):
  out = subprocess.check_output(prog_args_list, shell=run_in_shell)
  print(out.decode("utf-8"))

 
if __name__ == "__main__":
  print_command_output("ls", "-al")
