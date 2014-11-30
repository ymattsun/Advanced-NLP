#!/usr/bin/env python
# coding: utf-8

import sys, re

def AandB(FILE):
  AandB_list = []
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      AandB_list.append(mecab_list)
      i = len(AandB_list)-1
      if i > 1 and AandB_list[i-2][1] == '名詞' and AandB_list[i-1][0] == 'の' and AandB_list[i][1] == '名詞':
        print AandB_list[i-2][0], AandB_list[i-1][0], AandB_list[i][0]

if __name__ == '__main__':
  AandB(sys.argv[1])
