#!/usr/bin/env python
# coding:utf-8

import sys, re

#!/usr/bin/env python
# coding:utf-8

import sys, re

def post_pref_town(FILE):
  post_num, pref_name, town_name = [], [], []
  for line in open(FILE):
    line = line.strip().decode('utf-8')
    cols = line.split()
    if ur'([0-9]+)-([0-9]+)' in cols:
      post_num.append(cols)
    if ur'都|道|府|県|' in cols:
      pref_name.append(cols)
    if ur'区|市|町|村|郡' in cols:
      town_name.append(cols)
  
  post_pref_town_name = post_num + pref_name + town_name

if __name__ == '__main__':
  post_pref_town(sys.argv[1])
