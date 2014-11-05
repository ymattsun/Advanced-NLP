#!/usr/bin/env python
# coding:utf-8

import sys, re

def post_pref_town(FILE):
  for line in open(FILE):
    line = line.strip().decode('utf-8')
    #post_pref_town = re.compile(ur'([0-9]{3}-[0-9]{4})([一-龠]{2,3}(都|道|府|県|))(.{1,4}(区|市|町|村|郡))')
    pref_town = re.compile(ur'([一-龠]{2,3}(都|道|府|県|))(.{1,4}(区|市|町|村|郡))')

    #match_post_pref_town = post_pref_town.search(line)
    match_pref_town = pref_town.search(line)

    #if match_post_pref_town:
      #print match_post_pref_town.group(0)

    if match_pref_town:
      print match_pref_town.group(0)

if __name__ == '__main__':
  post_pref_town(sys.argv[1])
