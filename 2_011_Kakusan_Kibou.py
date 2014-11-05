#!/usr/bin/env python
# coding: utf-8

import sys

def Kakusan_Kibou(FILE):
  for line in open(FILE):
    line = line.decode('utf-8')
    if u'拡散希望' in line:
      sys.stdout.write(line.encode('utf-8'))

if __name__ == '__main__':
  Kakusan_Kibou(sys.argv[1])
