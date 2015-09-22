__author__ = 'eeamesX'
from lxml import etree
import lxml.etree as ET

import sys, os


try:
    __import__('prettytable')
    niceTable = True
except ImportError:
    niceTable = False
    pass


print "In order to use this script ..use python xmlcombine.py Arg1 Arg2 \n" \
      "Where Arg1 = filename you wish to take Elements from \n" \
      "Where Arg2= filename you wish to append elements into \n" \
      "Enter into promp element nodes you wish to move to Arg2.  No punctuation..just names!"
print 'lets combine a script using..', sys.argv[0]

filename = (sys.argv[1])
appendtoxml = (sys.argv[2])

print 'path =', filename
print 'full path =', os.path.abspath(filename)

askForNode1 = raw_input("What Element would you like to take? " )
request1 = ".//" + askForNode1

askForNode2 = raw_input("What other Element would you like to take? " )
request2 = ".//" + askForNode2

##Under constrction..if User doesnt select 2 nodes only one
if request2 == ".//no" or ".//No" or ".//":
    output_file = appendtoxml.replace('.xml', '') + "_editedbyed.xml"

    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(filename, parser)
    etree.tostring(tree)
    root = tree.getroot()

    a = root.findall(request1)

    print(" \n \n I am taking this info: \n \n")
    for r in a:
        print etree.tostring(r)
    out_tree = ET.parse(appendtoxml, parser)
    out_root = out_tree.getroot()
    for path in [request1]:
        for elt in root.findall(path):
            out_root.append(elt)

    print(" \n \n \n \n                                  Sucess!")
    print ("File creating successful, new file " + output_file + "created")
    print ("Path to this file you just created is ..\n" + os.path.dirname(output_file)
           )


    out_tree.write(output_file, pretty_print=True)
## ---------
else:
    output_file = appendtoxml.replace('.xml', '') + "_editedbyed.xml"
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(filename, parser)
    etree.tostring(tree)
    root = tree.getroot()


    a = root.findall(request1)
    b = root.findall(request2)


    print(" \n \n I am taking this info: \n \n")
    for r in a:
        print etree.tostring(r)
    for e in b:
        print etree.tostring(e)


    out_tree = ET.parse(appendtoxml, parser)
    out_root = out_tree.getroot()
    for path in [request1, request2]:
        for elt in root.findall(path):
            out_root.append(elt)


    print(" \n \n \n \n                                  Sucess!")
    print ("File creating successful, new file " + output_file + "created")
    print ("Path to this file you just created is ..\n" + os.path.dirname(output_file)
           )


    out_tree.write(output_file, pretty_print=True)

