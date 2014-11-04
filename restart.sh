#!/bin/bash

cp /Users/peterbryzgalov/work/docker-registry-driver-git/docker_registry/drivers/gitdriver.py /Users/peterbryzgalov/work/docker-registry/docker_registry/drivers/
# cp /Users/peterbryzgalov/work/docker-registry-driver-git/docker_registry/drivers/gitdriver_subproc.py /Users/peterbryzgalov/work/docker-registry/docker_registry/drivers/
rm -rf /Users/peterbryzgalov/tmp/gitrepo 
rm -rf /Users/peterbryzgalov/tmp/gitregistry 
rm -rf /private/tmp/docker-registry.db
rm -rf /Users/peterbryzgalov/tmp/git_tmp
rm /Users/peterbryzgalov/tmp/git_imagetable.txt
kill $(ps ax | grep ":5000" | awk '{ print $1 }')
./registry-start
