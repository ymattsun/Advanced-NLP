#!/usr/bin/env python
# coding: utf-8

def graphviz():
  print 'graph 7_069_graphviz{'
  for line in open('7_068_output.txt'):
    item = line.strip().split('\t')
    print '\t "%s" -- "%s" [label = "%s"];' % (item[1], item[2], item[0][0:5])
  print '}'

if __name__ == '__main__':
  graphviz()
