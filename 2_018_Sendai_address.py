#!/usr/bin/env python
# coding:utf-8

import sys, re

def sendai_address(address_FILE):
  sendai_add = []
  for line in open(address_FILE):
    line = line.strip().decode('utf-8')
    cols = line.split()
    if u'仙台市' in cols:
      sendai_add.append(cols)

  print sendai_add

if __name__ == '__main__':
  sendai_address(sys.argv[1])
