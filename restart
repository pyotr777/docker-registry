#!/bin/bash

./restart.py
kill $(ps ax | grep ":5000" | awk '{ print $1 }')
./registry-start
