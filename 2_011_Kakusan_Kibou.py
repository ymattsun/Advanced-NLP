#!/usr/bin/env python
# coding: utf-8

import sys

def Kakusan_Kibou(FILE):
  f = open(FILE)
  for line in f:
    line = line.decode('utf-8')
    if u'拡散希望' in line:
      sys.stdout.write(line.encode('utf-8'))
  f.close()

if __name__ == '__main__':
  Kakusan_Kibou(sys.argv[1])
