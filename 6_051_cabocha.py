#!/usr/bin/env python
# coding: utf-8

import sys

def cabocha(FILE):
  for line in open(FILE):
    print line

if __name__ == '__main__':
  cabocha(sys.argv[1])
