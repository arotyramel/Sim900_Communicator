#!/usr/bin/env python
print "creating python modules"
import subprocess
from os.path import dirname, basename, isfile, realpath
import os
import glob
dir_name = dirname(realpath(__file__))
path = dir_name+os.sep+"ui"+os.sep
modules = glob.glob(path+"*.ui")
for ui_file in [ basename(f)[:-3] for f in modules if isfile(f)]:     
    print "creating file:", path+ui_file+".py"
    cmd = ["pyside-uic", path+ui_file+".ui"]
    with open(path+ui_file+".py","w") as f:
        try:
            res = subprocess.check_output(cmd)
        except Exception as exc:
            print exc
        f.write(res)
        