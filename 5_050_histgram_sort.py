#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from collections import defaultdict

def histgram_sort():
  hist = []
  freq = defaultdict(int)

  for line in open("line_freq.txt"):
    line = line.strip().split("\t")
    if line != None:
      hist.append(int(line[1]))

  fig = plt.figure()
  ax = fig.add_subplot(111)

  i = 1
  for i in range(101):
    plt.plot(i, hist[i - 1], 'bo')
 
  plt.title('histgram_sort')
  plt.xlabel(' Ranking ')
  plt.ylabel(' Freqency ')
  ax.set_xlim(1, 30)
  ax.set_ylim(0, 150)
  plt.savefig('plt_5_050.png')
  plt.show()

if __name__ == '__main__':
  histgram_sort()
