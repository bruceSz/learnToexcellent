#!/usr/bin/python
import markdown
import codecs

#open input file in read,utf-8 mode
input_file=codecs.open('notes.txt',mode='r',encoding="utf8")
text = input_file.read()
html = markdown.markdown(text)

#print
print html

#Write string html to disk

output_file = codecs.open('notes_py.html',mode='w',encoding="utf8")
output_file.write(html)
