
__author__ = 'eeamesX'
import os, sys


directory = sys.argv[1]




for root, dirs, files in os.walk(directory):
    if len(files) >= 3:
        for f in files:
            print(os.path.join(root, f))

            if f.endswith(".csv"):
                print f + " made it this far"
                with open(os.path.join(root, f), "r") as d:
                    for line in d:
                        print line