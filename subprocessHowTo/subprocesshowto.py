'''
Created on Mar 2, 2017

@author: jackwang
'''
import subprocess
from subprocess import Popen, PIPE


ls_output = subprocess.call('ls -l', shell=True)
print ls_output

Popen(['xterm', '-e', 'sleep 3s'])

