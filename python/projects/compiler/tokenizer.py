import re

#globals
#alltable={0:reserved_words,1:separators,2:opetrators,3:ids,4:const_values}

#0
reserved_words=('int','for','break','continue','include','define','return','do','while')
#1
separators=('(',')','{','}',';',',',':','[',']','|')
#2
operators = ('+','-','*','/','<','=','>')
#3
ids=[]
#4
const_values=(
    [],#0 int
)
text = ""
file_name = 'long.c'

def preprocess():
    global text,file_name
    i = 0
    reduce_line_regex = re.compile(r"(\\[ \t\r]*\n)")
    with open(file_name) as in_file:
	for line in in_file:
	    i+=1
	    text+=reduce_line_regex.sub("",line)

