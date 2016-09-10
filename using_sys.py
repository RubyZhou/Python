#!/usr/bin/python
#Filename : using_sys.py

import sys


print 'The command line arguments are:'
for i in sys.argv:
	print i

print 'Output argv[0]:',sys.argv[0]

print 'Output argv[1]:',sys.argv[1]


print '\n\nThe PYTHON_PATH is ',sys.path,'\n'
