#!/usr/bin/env python
# coding: utf-8

import sys

def view_words(FILE):
  dictionaly = {}
  for line in open(FILE):
    word_list = line.strip().split('|')
    dictionaly[word_list[0]] = (word_list[1], word_list[3], word_list[6])
    print dictionaly

if __name__ == '__main__':
  view_words(sys.argv[1])
