#!/usr/bin/python3
import subprocess

file_name = input()

code = subprocess.call(['rar', 'x', '-p-', file_name])
password = ''
while(code):
  try:
    password = input()
    code = subprocess.call(['unrar', 'x', '-p' + password, file_name])
    print(password)
  except EOFError:
    break
else:
  print('Password successful!')

