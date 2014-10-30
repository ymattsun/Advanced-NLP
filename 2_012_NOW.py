#!/usr/bin/env python
# coding: utf-8

import sys

def NOW(FILE):
  f = open(FILE)
  for line in f:
    line = line.strip().decode('utf-8')
    if line[-2:] == u'なう':
      sys.stdout.write('%s\n' % line.encode('utf-8'))

if __name__ == '__main__':
  NOW(sys.argv[1])
