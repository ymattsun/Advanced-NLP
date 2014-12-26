#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import sys

def make_vector(FILE):
  word_dict = defaultdict(list)
  for line in open(FILE):
    for item in line.strip().split('\t'):
      relate_value = item.split(' : ')
      if len(relate_value) == 1:
        word = relate_value[0]
      else:
        word_dict[word].append((relate_value[0], relate_value[1]))
  return word_dict

def calculate_vector(word_dict, argv1, argv2):
  i = 0
  for word1, v1 in word_dict[argv1]:
    for word2, v2 in word_dict[argv2]:
      if word1 == word2:
        i += float(v1) * float(v2)

  return str(i)

if __name__ == '__main__':
  word_dict = make_vector("7_066_output.txt")
  print 'result = ', calculate_vector(word_dict, sys.argv[1], sys.argv[2])
