#!/usr/bin/env python
# coding: utf-8

import sys, re

def RT(FILE):
  RTcomment = re.compile(ur'.*RT @[a-zA-Z0-9_]+: ')
  f = open(FILE)
  for line in f:
    line = line.decode('utf-8')
    if RTcomment.match(line):
      print RTcomment.sub('', line).encode('utf-8')
  f.close()

if __name__ == '__main__':
  RT(sys.argv[1])
