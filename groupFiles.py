__author__ = 'ed'

import os, sys
import re
import shutil
from collections import defaultdict

directoryChosen = sys.argv[1]




for f in os.listdir(directoryChosen):
    fname, fext = os.path.splitext(f)
    if not f.startswith('.'):
        print f

        print fname + " Is fname"
        dest_path = fname
        print dest_path + " is dest path"
        print fname + "this is fname"
        if os.path.isdir(directoryChosen + '/' + fname):
            print "Ended here/ Start work here"
            shutil.copy2(directoryChosen + '/' + f, directoryChosen + '/' + dest_path)
        if not os.path.isdir(directoryChosen + '/' + fname):
            print "working here kind of..lets make directories"

            os.mkdir(dest_path)
            print " Path is created"

            shutil.copy2(directoryChosen + '/' + f, directoryChosen + '/' + dest_path)
