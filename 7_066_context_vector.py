#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import sys, math

def make_dict(FILE):
  for line in open(FILE):
    word, text = line.strip().split('\t')
    cnt[word][text] += 1

def make_vector():
  for word in cnt.keys():
    i = 0
  for k, v in cnt[word].items():
    i += v * v

  dict_norm[word] = math.sqrt(i)

def context_vector():
  for word in cnt.keys():
    sys.stdout.write(word)
    for k, v in cnt[word].items():
      sys.stdout.write('\t' + k + ' : ' + str(float(v)/dict_norm[word]))
    print ''

if __name__ == '__main__':
  cnt = defaultdict(lambda: defaultdict(int))
  dict_norm = defaultdict(lambda: 0)
  make_dict('7_065_output.txt')
  make_vector()
  context_vector()
