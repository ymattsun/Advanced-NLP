#!/usr/bin/env python
# coding:utf-8

import sys

def char_diff(FILE):
  f = open(FILE).readlines()
  print len(set(f))
  
if __name__ == '__main__':
  char_diff(sys.argv[1])
