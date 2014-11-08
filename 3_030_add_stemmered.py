#!/usr/bin/env python
# coding: utf-8

import sys, re
from porter2 import stem

def add_stemmered(word):
  porter_stemmered = open("porter_stemmered.txt", "w")
  for line in open(word):
    line = line.strip().split('\t')
    if line[0] != '':
      print (line[0] + '\t' + line[1] + '\t' + stem(line[1]))
      porter_stemmered.write(line[0] + '\t' + line[1] + '\t' + stem(line[1]) + '\n')

  porter_stemmered.close()

if __name__ == '__main__':
  add_stemmered(sys.argv[1])
