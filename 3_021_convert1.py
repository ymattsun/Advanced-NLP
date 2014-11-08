#!/usr/bin/env python
# coding: utf-8

import sys

def convert(text):
  #convert1 = open("convert1.txt", "w")
  for line in open(text):
    for sent in line.strip().rstrip('.').split('. '):
      print sent + '.\n'
      #convert1.write(sent + '.\n')
  
  #convert1.close()

if __name__ == '__main__':
  convert(sys.argv[1])
