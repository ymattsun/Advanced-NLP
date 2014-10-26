#!/usr/bin/env python
# coding:utf-8

import sys

def paste(FILE1, FILE2):
  f1, f2 = open(FILE1), open(FILE2)
  for i in range(sum([ 1 for line in open(FILE1) ])):
    print '%s\t%s' % (f1.readline().strip(), f2.readline().strip())
  f1.close()
  f2.close()

if __name__ == '__main__':
  paste(sys.argv[1], sys.argv[2])
