#!/usr/bin/env python
# coding: utf-8

import sys, re

def emoji(file_line):
  emoji_kigou_pattern = re.compile(ur'([[(]（]+)(.+?)([[)]|）]+)')
  #kanji_pattern = re.compile(ur'[一-龠]+')
  result = re.match(emoji_kigou_pattern, file_line)
  if result != None:
    return emoji_kigou_pattern

if __name__ == '__main__':
  emojis = {}
  for line in open(sys.argv[1]):
    #line = line.strip().decode('utf-8')
    #emojis = emoji(line)
    #print ''.join(emojis).encode('utf-8')
