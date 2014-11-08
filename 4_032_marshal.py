#!/usr/bin/env python
# coding: utf-8

import sys, marshal
from view_words import view_words

if __name__ == '__main__':
  marshal.dump(view_words(sys.argv[1]), open("inflection_dict.txt", 'w'))
