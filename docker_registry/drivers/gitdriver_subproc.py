# Wait while _inprocess file is removed from directory
# and make commit

import gitdriver
import sys, time, os

version="0.1"

path = sys.argv[1]
storage=sys.argv[2]
print "gitdriver_subproc v."+version+"\nWatch " + path
while os.path.exists(path):
    time.sleep(1)
print "Continue with commit"
storage.printSettings()