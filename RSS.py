#!/usr/bin/env python
# encoding: utf-8

import commands
import os
import re
out = commands.getoutput('ls /proc/ | grep "^[0-9]"')
listresult = re.split(r'(\n)',out)
rem = 0
for pid in listresult:
    filepath = "/proc/" + pid + "/statm"
    if os.path.exists(filepath):
        #print filepath
        with open(filepath) as f:
            for line in f:
                #txt = re.split(r'(\s)',line)
                txt = line.split(' ')
                rem += int(txt[2])
print rem



