#!/usr/bin/python3
## -*- coding: utf-8 -*-
import sys
import re
import sqlite3

con = sqlite3.connect('./text_data.sqlite')
cur = con.cursor()
cur.execute('SELECT pref, word FROM WORDS;')
items=cur.fetchall()
f=open('./word_list.txt','w')
for item in items:
	word=item[1]
	f.write(word+'\n')
cur.close()
con.close()
f.close()
