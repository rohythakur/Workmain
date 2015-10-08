__author__ = 'eeamesX'
import os, sys
import re
import shutil
from collections import defaultdict

directoryChosen = sys.argv[1]





for f in os.listdir(directoryChosen):

    if not f.startswith('.'):
        print f + " this is the file"

        fname, fext = os.path.splitext(f)
        print fname + "                  Is fname"
        dest_path = fname



        source = directoryChosen + f
        destination = directoryChosen + dest_path


        print source + "                   this is source"
        print destination + "             this is destination"
        print dest_path + "               is dest path"
        print fname + "                   this is fname"


        if not os.path.isdir(destination):


            os.mkdir(destination)
            print " Path is created ..maiking directory here"
            print " Path is created ..maiking directory here"
            print " Path is created ..maiking directory here"
            print " Path is created ..maiking directory here"


            shutil.copy(source, dest_path)

        if os.path.isdir(destination):

            print "Ended here/ Start work here"
            shutil.copy(source, destination)
