#!/usr/bin/env python
# coding: utf-8

import sys, re

def ness_ly(word):
  nessly = re.compile(r'.*(ly$|ness$)')
  if nessly.match(word):
    return word
  return None

if __name__ == '__main__':
  for line in open(sys.argv[1]):
    if ness_ly(line) != None:
      print line
