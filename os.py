#!/usr/bin/python

import os, sys

print(os.name)
print(os.uname())

import platform
print(platform.system())

import os
cmd = 'ls -l'
os.system(cmd)
os.system('ping google.com')


# Open a file
path = "/home/thanos"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print(file)

#os.mkdir('/home/thanos/test_dir')
