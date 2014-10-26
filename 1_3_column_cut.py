#!/usr/bin/env python
# coding:utf-8

import sys

def column_cut(FILE):
  f = open(FILE)
  col_1 = open('col1.txt', 'w')
  col_2 = open('col2.txt', 'w')
  
  for line in f:
    line = line.rstrip()
    cut = line.split('\t')
    
    try:
      col_1.write(cut[0] + '\n')
      col_2.write(cut[1] + '\n')
    except:
      col_1.write('')
      col_2.write('')
  
  f.close()
  col_1.close()
  col_2.close() 

if __name__ == '__main__':
  column_cut(sys.argv[1])
