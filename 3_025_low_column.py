#!/usr/bin/env python
# coding: utf-8

import sys

def low_column(word):
  #low_column = open("low_column.txt", "w")
  for line in open(word):
    sys.stdout.write('%s\t%s' % (line.strip(), line.lower()))
    #low_column.write('%s\t%s' % (line.strip(), line.lower()))

  #low_column.close()

if __name__ == '__main__':
  low_column(sys.argv[1])
