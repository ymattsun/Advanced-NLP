#!/usr/bin/env python
# coding: utf-8

import sys

def word_joint():
  #word_joint = open("word_joint.txt", "w")
  prev = ''
  for line in open("split_words1.txt"):
    line = line.strip()
    if prev and line:
      print prev + '\t' + line
      #word_joint.write(prev + '\t' + line + '\n')
    
    prev = line

  #word_joint.close()

if __name__ == '__main__':
  word_joint()
