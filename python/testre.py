#!/usr/bin/python
import re
commit_pattern='^commit'
str='commitdd fjdkie commit ksjke\ncommit'
tmp=re.findall(commit_pattern,str)
if tmp:
	print (tmp[0])
#if m:
#	print(m.string())
