#!/usr/bin/env python
# coding:utf-8

import sys

def Head_Ncount(FILE, N):
  f = open(FILE)
  for i in range(N):
    sys.stdout.write(f.readline())
  f.close()

if __name__ == '__main__':
  Head_Ncount(sys.argv[1], int(sys.argv[2]))
