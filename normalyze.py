#!/usr/bin/python3
## -*- coding: utf-8 -*-
import sys
import re
import sqlite3

#f=open('./RU_UTF.dic','r')
#lines=f.read()
#con = sqlite3.connect('./text_data.sqlite')
#cur = con.cursor()
#for line in lines.split('\n'):
#	word=line.upper().split("/")[0]
#	try:
#		preffix=line.upper().split("/")[1]
#	except:
#		preffix=''
#	try:
#		cur.execute('INSERT INTO WORDS (pref, word) VALUES (\''+preffix+'\',\''+word+'\')')
#		con.commit()
#	except:
#		con.commit()
#	print (word)
#cur.close()
#con.close()

#con = sqlite3.connect('./text_data.sqlite')
#cur = con.cursor()
#cur.execute('SELECT pref, word FROM WORDS;')
#items=cur.fetchall()
#for item in items:
#	word=item[1]
#	cur.execute('SELECT id FROM  WORDS WHERE word=\''+word+'\'')
#	bid=cur.fetchone()[0]
#	f=open('./RU_UTF.aff','r')
#	print (item)
#	lines=f.read()
#	for line in lines.split('\n'):
#		line=line.upper()
#		line=re.sub(' +',' ',line).split(' ')
#		operate=False
#		try:
#			# Check for ready
#			for character in item[0]:
#				if line[1]==character:
#					selector=line[4]
#					operate=True
#		except:
#			operate=False
#		if operate:
#			try:
#				operate=line[4].split(']')[0].split('[')[1]
#				static=line[4].split(']')[1]
#			except:
#				operate=''
#				static=line[4]
#			new_word=''
#			if word[len(word)-(len(static)):len(word)]==static and word[len(word)-(len(static)):len(word)]==line[2]:
#				# Mode without operate
#				if operate=='':
#					new_word=word[:-(len(line[2]))]+line[3]
#				else:
#					# Reverse operate
#					if operate[0]=='^':
#						r_items=operate[1:]
#						for r_item in r_items:
#							#print ("Reverse operate:"+r_item)
#							if word[len(word)-(len(static))-1:len(word)-(len(static))]!=r_item:
#								new_word=word[:-(len(line[2]))]+line[3]
#					# Direct operate
#					if operate[0]!='^':
#						r_items=operate[:]
#						for r_item in r_items:
#							#print ("Reverse operate:"+r_item)
#							if word[len(word)-(len(static))-1:len(word)-(len(static))]==r_item:
#								new_word=word[:-(len(line[2]))]+line[3]
#				if new_word!='':
#					try:
#						cur.execute('INSERT INTO WORDS (pref, word) VALUES (\'\',\''+new_word+'\')')
#						con.commit()
#					except:
#						con.commit()
#					cur.execute('SELECT id FROM  WORDS WHERE word=\''+new_word+'\'')
#					sid=cur.fetchone()[0]
#					cur.execute('UPDATE WORDS SET base_id='+str(bid)+' WHERE id=\''+str(sid)+'\'')
#					print ('>'+new_word+' '+str(sid)+'<>'+str(bid))
#	f.close()
#cur.close()
#con.close()


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
