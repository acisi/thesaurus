#!/usr/bin/python3
## -*- coding: utf-8 -*-
import sys
import re
import sqlite3

#con = sqlite3.connect('./text_data.sqlite')
#cur = con.cursor()
#f=open('./anekdot_list.txt','r')
#lines=f.read()
#text=''
#for line in lines.split('\n'):
#	if line.count('==[acisi]==')>0:
#		# Удаляем знаки припинания
#		text=text.replace('!',' ')
#		text=text.replace('.',' ')
#		text=text.replace(',',' ')
#		text=text.replace('-',' ')
#		text=text.replace('(',' ')
#		text=text.replace(')',' ')
#		text=text.replace('?',' ')
#		text=text.replace('"',' ')
#		text=text.replace("'",' ')
#		text=text.replace(":",' ')
#		# Upcase text
#		text=text.upper()
#		# Replace Double Space
#		text=re.sub(' +',' ',text)
#		# Split text to words
#		for word in text.split(' '):
#			print (word)
#		text=''
#		sys.exit()
#	else:
#		text=text+line
#f.close()
