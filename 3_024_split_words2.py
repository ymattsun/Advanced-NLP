#!/usr/bin/env python
# coding: utf-8

import sys, re

def split_words2(textline):
  #split_words2 = open("split_words2.txt", "w")
  kigou = re.compile(r'(\,$|\.$|\($|\)$|\%)')

  for line in open(textline):
    line = line.strip().split()
    for word in line:
      match = kigou.search(word)
      if match:
        print re.sub(r'(\,$|\.$|\($|\)$|\%)', r'\n\1', word)
        #split_words2.write(re.sub(r'(\,$|\.$|\($|\)$|\%)', r'\n\1\n', word))
      else:
        print word
        #split_words2.write(word + '\n')
        
    print ''
    #split_words2.write('\n')

  #split_words2.close()

if __name__ == '__main__':
  split_words2(sys.argv[1])
