#!/usr/bin/env python
# coding:utf-8

import sys, re

def sendai_address(address_FILE):
  for line in open(address_FILE):
    line = line.strip().decode('utf-8')
    if u'仙台市' in line:
      print line.encode('utf-8') + '\n'

if __name__ == '__main__':
  sendai_address(sys.argv[1])
