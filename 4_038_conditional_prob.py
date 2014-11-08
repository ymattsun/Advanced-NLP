#!/usr/bin/env python
# coding: utf-8

import sys
from collections import Counter

def cond_prob():
  cond_prob = open("cond_prob.txt", "w")

  prob_w, prob_z = Counter(), Counter()

  for line in open("word_count.txt"):
    line = line.strip().split('\t')
    prob_z[str(line[1]) + '\t' + str(line[2])] += 1
    prob_w[str(line[1])] += 1
    
  for word in prob_z:
    word_list = word.strip().split('\t')
    prob = float(prob_z[word]/prob_w[word_list[0]])
    print str(prob) + '\t' + word
    cond_prob.write(str(prob) + '\t' + word + '\n')

  cond_prob.close()

if __name__ == '__main__':
  cond_prob()
