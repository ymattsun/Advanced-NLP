#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import sys

def dist_two_class(class1, class2):
  cos_min = 1.0
  for word1 in class1: 
    for word2 in class2:
      if not word1 + ' ' + word2 in dict:
        dict[word1 + ' ' + word2] = 1.0

      if dict[word1 + ' ' + word2] < cos_min:
        cos_min = dict[word1 + ' ' + word2]

    if cos_min ==1:
      cos_min = 0

    return cos_min

def furthest_neighbor_method(argv1):
  dict = defaultdict(lambda: 0)
  word_set =set([])
  for line in open('7_068_output.txt'):
    item = line.strip().split('\t')
    dict[item[1] + ' ' + item[2]] = float(item[0])
    dict[item[2] + ' ' + item[1]] = float(item[0])
    word_set.add(item[1])
    word_set.add(item[2])

  class_list = []
  for word in word_set:
    word = [word]
    class_list.append(word)

  while len(class_list) > int(argv1):
    d_max = 0
    best_class = tuple
    for class1 in class_list:
      for class2 in class_list:
        if class1 != class2:
          d = dist_two_class(class1, class2)
          if d >= d_max:
            d_max = d_max
            best_class = (class1, class2)

    class1, class2 = best_class[0], best_class[1]
    class_list.append(best_class[0] + best_class[1])
    class_list.remove(best_class[0])
    class_list.remove(best_class[1])

    print len(dict)
    max_word1, max_word2 = max(dict.items(), key = lambda x:x[1])[0].split()
    print max_word1, max_word2

if __name__ == '__main__':
  furthest_neighbor_method(sys.argv[1])
