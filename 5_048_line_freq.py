#!/usr/bin/env python
# coding: utf-8

import sys, re
from collections import Counter
list_dict=[]

def line_freq(FILE):
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      if mecab_list[1] == "動詞":
        list_dict.append(mecab_list[7])

  counter = Counter(list_dict)

  #f = open('line_freq.txt', 'w')

  for word, count in sorted(counter.most_common(), key = lambda x:x[1], reverse = True):
    print word, count
    #f.write(word + '\t' + str(count) + '\n')

  #f.close()

if __name__ == '__main__':
  line_freq(sys.argv[1])
