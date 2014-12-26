#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
from japan_mycountry import *

def inter_product():
  result = defaultdict(lambda: 0)
  word_dict = make_vector('7_066_output.txt')
  for word1 in word_dict:
    for word2 in word_dict:
      if word1 != word2:
        if word2 + ' ' + word1 not in result:
          result[word1 + ' ' + word2] = calculate_vector(word_dict, word1, word2)

  return result

def sort_dict(result):
  for word, i in sorted(result.items(), key = lambda x:x[1], reverse = True):
    if float(i) >= 0.4:
      print (i + '\t' + word.split()[0] + '\t' + word.split()[1])

if __name__ == '__main__':
  sort_dict(inter_product())
