#!/usr/bin/env python
# coding:utf-8

import sys

def sort_col2_col1_reverse(FILE):
  f = open(FILE)
  File_Line = []
  for line in f:
    cut = line.strip('\t').split('\n')
    File_Line.append(cut)

  File_Line.sort(key=lambda x:(x[1], x[0]), reverse = True)

  for i in File_Line:
    print i[0] + '\t' + i[1]
  f.close()

if __name__ == '__main__':
  sort_col2_col1_reverse(sys.argv[1])
