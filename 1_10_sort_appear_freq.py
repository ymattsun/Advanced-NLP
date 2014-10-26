#!/usr/bin/env python
# coding:utf-8

import sys
from collections import Counter

def sort_appear_freq(FILE):
  f = open(FILE)
  All_Lines = Counter(f.readlines())

  Line_sort = sorted(All_Lines.most_common(), key = lambda x:x[1], reverse = True)

  for i in Line_sort:
    print i[0].strip('\n') + '\t' + str(i[1])
  f.close()

if __name__ == '__main__':
  sort_appear_freq(sys.argv[1])
