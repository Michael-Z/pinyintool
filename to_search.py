#!/usr/bin/env python
#coding=utf-8
import os
f = open("to_search_new.txt","r")
w = open('to_search_new_finish', 'w')
linesz = f.readlines()
for line in linesz:
	commandstr = "pypinyin " + line.strip() + " -s TONE3"
	ret1 = os.popen( commandstr ).read()
	print line.strip()
	w.write( line.strip() + " " + ret1.strip().upper())
	w.write("\r\n")

f.close()
w.close()
