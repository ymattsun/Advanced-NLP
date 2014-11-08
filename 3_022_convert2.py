#!/usr/bin/env python
# coding: utf-8

import sys, re

def convert2(text):
  #convert2 = open("convert2.txt", "w")
  for line in open(text):
    line = line.strip()
    print re.sub(r'\. ([A-Z])', r'.\n\n\1', line)
    #convert2.write(re.sub(r'\. ([A-Z])', r'.\n\1', line))

  #convert2.close()

if __name__ == '__main__':
  convert2(sys.argv[1])
