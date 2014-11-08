#!/usr/bin/env python
# coding:utf-8

import sys
from collections import Counter

def sort_appear_freq(FILE):
  count = 0
  All_Lines = Counter(open(FILE).readlines())
  Line_sort = sorted(All_Lines.most_common(), key = lambda x:x[1], reverse = True)

  del Line_sort[0]

  for i in Line_sort:
    count += 1
    if count <= 100:
      print str(count) + '\t' + i[0].strip('\n') + '\t' + str(i[1])

if __name__ == '__main__':
  sort_appear_freq(sys.argv[1])
