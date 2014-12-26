#!/usr/bin/env python
# coding: utf-8

def sort_tf_idf():
  import re
  dict = {}

  for line in open('7_063_output_tf_idf.txt'):
    word, tf_idf = line.strip().split('\t')
    num = re.compile(r'[0-9]')
    if not num.search(word):
      dict[word] = float(tf_idf)

  return dict

def tf_idf_top100(dict):
  j = 0
  for word, i in sorted(dict.items(), key = lambda x:x[1], reverse = True):
    j += 1
    if j <= 100:
      print word, i

if __name__ == '__main__':
  tf_idf_top100(sort_tf_idf())
