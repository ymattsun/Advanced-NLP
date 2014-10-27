#!/usr/bin/env python
# coding: utf-8

import sys, re

def Capital_Kanji(line):
  #kanji = re.compile(ur'([一-龠]+)')
  #cap = re.compile(ur'[(]([A-Z]+)')
  cap_kanji = re.compile(ur'([一-龠]+)[(]([A-Z]+)')
  m = cap_kanji.search(line)
  if m != None:
    return m.groups()

def openFile(FILE):
  for line in open(FILE):
    line = line.decode('utf-8')
    groups = Capital_Kanji(line)
    if groups != None:
      print groups[0] + '\t' + groups[1]

if __name__ == '__main__':
  openFile(sys.argv[1])
