#!/usr/bin/env python
# coding: utf-8

import sys, re

def emoji(file_line):
  left_parts = re.compile(ur'([\]*)([(]*)')
  face_parts = re.compile(ur'([一-龠]+)[^\"!?<>+#$%&~|][a-zA-Z0-9]')
  right_parts = re.compile(ur'([)]*)([/]*)')
  
  kaomoji = left_parts + face_parts + right_parts
  result = kaomoji.search(file_line)
  if result != None:
    return result.groups()

if __name__ == '__main__':
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    emoji_groups = emoji(line)
    if emoji_groups != None:
      print emoji_groups
