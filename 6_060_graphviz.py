#!/usr/bin/env python
# coding: utf-8

def graphviz():
  print 'digraph 6_060_graphviz{'
  for line in open('not_independent.txt'):
    item = line.replace('\"', r'\"')
    item = item.strip().split('\t')
    print '\t"%s" -> "%s";' % (item[0], item[1])
  print '}'

if __name__ == '__main__':
  graphviz()
