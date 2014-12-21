#!/usr/bin/env python
# coding: utf-8

import sys, re, glob, math
from collections import defaultdict

def make_dict():
  set_list=[]
  all_dict = defaultdict(lambda: 0) 
  N = len(glob.glob('7_062_output_?.txt'))

  for num in glob.glob('7_062_output_?.txt'):
    word_set = set([])
    for line in open(num):
      line = line.strip()
      word_set.add(line)
      all_dict[line] += 1

    set_list.append(word_set)

  return all_dict, set_list, N

def tf_idf(all_dict, set_list, N):
  for word, ii in sorted(all_dict.items(), key = lambda x:x[1], reverse = True):
    i = 0
    for word_set in set_list:
      if word in word_set:
        i += 1

    print '%s\t%.6f\t%d\t%d' % (word, (all_dict[word]*math.log(float(N)/i,2)), all_dict[word], i)

if __name__ == '__main__':
  all_dict, set_list, N = make_dict()
  tf_idf(all_dict, set_list, N)
