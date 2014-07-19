#!python3


import subprocess

def print_command_output(prog, args, run_in_shell=False):
  out = subprocess.check_output([prog, args], shell=run_in_shell)
  print(out.decode("utf-8"))

 
if __name__ == "__main__":
  print_command_output("ls", "-al")
