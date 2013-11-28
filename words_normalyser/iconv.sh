#!/bin/sh
cat ./word_list.txt | iconv -f UTF-8 -t WINDOWS-1251 > ./word_list_cp1251.txt

