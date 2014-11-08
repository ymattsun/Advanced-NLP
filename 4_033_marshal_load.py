#!/usr/bin/env python
# coding: utf-8

import sys, marshal

if __name__ == '__main__':
  words_list = []
  words_dict = marshal.load(open('inflection_dict.txt'))
  for line in words_dict:
    words_list.append(line)
  
  for line in open("porter_stemmered.txt"):
    line = line.strip().split("\t")
    if line[1] in words_list:
      print ("'" + line[1] + "'" + " is here!")
    else:
      print ("'" + line[1] + "'" + " is not here...")
