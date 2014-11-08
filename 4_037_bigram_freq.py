#!/usr/bin/env python
# coding: utf-8

import sys
from collections import Counter

def word_count():
  #word_count = open("word_count.txt", "w")

  word_list = []
  for line in open("word_joint.txt"):
    line = line.strip()
    word_list.append(line)
  
  count = Counter(word_list)
  
  for word, cnt in sorted(count.most_common(), key = lambda x:x[1], reverse = True):
    print str(cnt) + '\t' + word
    #word_count.write(str(cnt) + '\t' + word + '\n')

  #word_count.close()

if __name__ == '__main__':
  word_count()
