#!/usr/bin/python
# first attempt
# - just print whatever is passed in to stdin
# - if filename passed in, print file instead of stdin

import fileinput
import re

def convertStrong(line):
	line = re.sub(r'\*\*(.*)\*\*',r'<strong>\1</strong>',line)
	line = re.sub(r'__(.*)__',r'<strong>\1</strong>',line)
	return line
def convertEm(line):
	line = re.sub(r'\*(.*)\*',,line)
for line in fileinput.input():
	print line, # print the line,the comma says don't add a newline between them

