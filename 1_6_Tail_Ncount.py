#!/usr/bin/env python
# coding:utf-8

import sys

def Tail_Ncount(FILE, N):
  f = open(FILE)
  File_Line_count = f.readlines()

  for i in range(len(File_Line_count) - N, len(File_Line_count)):
    sys.stdout.write(File_Line_count[i])
  f.close()

if __name__ == '__main__':
  Tail_Ncount(sys.argv[1], int(sys.argv[2]))
