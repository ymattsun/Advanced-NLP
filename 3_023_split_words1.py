#!/usr/bin/env python
# coding: utf-8

import sys

def split_words(textline):
  #split_words1 = open("split_words1.txt", "w")
  for line in open(textline):
    words = line.strip().split()
    for word in words:
      print word
      #split_words1.write(word + '\n')
    print ''
    #split_words1.write('\n')

  #split_words1.close()

if __name__ == '__main__':
  split_words(sys.argv[1])
