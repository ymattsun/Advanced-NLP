#!/usr/bin/env python
# coding: utf-8

import sys, marshal
from collections import Counter

if __name__ == '__main__':
  count = Counter()  

  words_list = []
  words_dict = marshal.load(open('inflection_dict.txt'))
  for line in words_dict:
    words_list.append(line)
  
  for line in open("porter_stemmered.txt"):
    line = line.strip().split("\t")
    if line[1] in words_list:
      count[line[1]] += 1
      if count[line[1]] >= 3:
        print "'" + line[1] + "'" + " is more than 3 entries!"
