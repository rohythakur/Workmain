__author__ = 'eeamesX'
import os, sys

directorySelected = sys.argv[1]
print directorySelected
filelist = [ f for f in os.listdir(directorySelected) if f.endswith(".csv") or f.endswith(".xml") or f.endswith(".wav") ]
for f in filelist:
    if not f.startswith('.'):
        print f + " Is a file"
        os.remove(directorySelected + '/' + f)
