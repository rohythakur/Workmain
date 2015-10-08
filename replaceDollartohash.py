
__author__ = 'eeamesX'
import os, sys

directoryChosen = (sys.argv[1])

print directoryChosen + "   thi is inside dollartohash"
if os.path.isdir(directoryChosen):
    for n in os.listdir(directoryChosen):
        if not n.startswith('.'):

            newname =  n.replace('$', '#')
            print newname
            if newname != n:
                path = os.path.join(directoryChosen, n)
                print path + "    this is path"
                target = os.path.join(directoryChosen, newname)
                print target + "   this is target"
                os.rename(path, target)

    newdir = directoryChosen.replace('$', '#')
    print newdir
    if directoryChosen != newdir :
         os.rename(directoryChosen, newdir)