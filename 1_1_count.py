#!/usr/bin/env python
# coding:utf-8

import sys

def count(line_count):
  f = open(line_count)
  print sum([1 for line in f])

if __name__ == '__main__':
  count(sys.argv[1])
