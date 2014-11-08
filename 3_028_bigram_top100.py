#!/usr/bin/env python
# coding: utf-8

import sys
from sort_appear_freq import *

def bigram(word):
  bigram = open('bigram.txt', 'w')
  for line in open(word):
    line = line.strip().decode('utf-8')
    if len(line) <= 2:
      bigram.write(line.encode('utf-8') + '\n')
      continue
    for i in range(len(line) - 1):
      bigram.write('%s%s\n' % \
                  (line[i].encode('utf-8'), line[i + 1].encode('utf-8')))

  bigram.close()

if __name__ == '__main__':
  bigram(sys.argv[1])
  sort_appear_freq('bigram.txt')
