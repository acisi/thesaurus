#!/usr/bin/python3
## -*- coding: utf-8 -*-
import sys
import re
import sqlite3
import psycopg2

f=open('./th_ru_RU_v2.dat','r')
lines=f.read()
con = sqlite3.connect('./text_data_upload.sqlite')
cur = con.cursor()
cur.execute('SELECT word,synonim FROM thesaurus;')
items=cur.fetchall()
p_conn=psycopg2.connect('host=127.0.0.1 dbname=dictionary user=postgres')
p_cur=p_conn.cursor()
for item in items:
	print(item)
#	if item[2]==None:
#		bwid=0
#	else:
#		bwid=item[2]
#	if item[1]!='':
	try:
		p_cur.execute('INSERT INTO thesaurus(word_id, synonym)  VALUES ('+str(item[0])+','+str(item[1])+');')
		p_conn.commit()
	except:
		p_conn.commit()
p_cur.close()
p_conn.close()
cur.close()
con.close()

