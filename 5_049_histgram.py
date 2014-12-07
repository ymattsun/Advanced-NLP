#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from collections import defaultdict

def histgram():
  hist = []
  freq = defaultdict(int)

  for line in open("line_freq.txt"):
    line = line.strip().split("\t")
    if line != None:
      hist.append(int(line[1]))

  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.hist(hist, bins = 100, range = (1, 200))

  plt.title('histgram')
  plt.xlabel(' Frequency ')
  plt.ylabel(' Number of types ')
  ax.set_xlim(1, 200)
  ax.set_ylim(0, 500)
  plt.savefig('plt_5_049.png')
  plt.show()

if __name__ == '__main__':
  histgram()
