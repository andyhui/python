#!/usr/bin/env python
# encoding: utf-8

import os
os.makedirs("test/multiple/levels")

fp = open("test/multiple/levels/files","w")
fp.write("inspector praline")
fp.close()

os.remove("test/multiple/levels/files")

os.removedirs("test/multiple/levels")
