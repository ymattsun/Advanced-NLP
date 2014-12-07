#!/usr/bin/env python
# coding: utf-8

import sys, re

def mecab(FILE):
  result = []
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      dict = {'surface': mecab_list[0], 'base' : mecab_list[7] , 'pos': mecab_list[1], 'pos1': mecab_list[2]}
      result.append(dict)
  
  for i in result:
    for k, w in i.items():
      print k, w
    print ""

if __name__ == '__main__':
  mecab(sys.argv[1])
