#!/usr/bin/env python
# encoding: utf-8

import os


def deldir(root):
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
        os.rmdir(root)


def remove(root, subdir):
    for f in os.listdir(root):
        file = os.path.join(root, f)
        if os.path.isdir(file):
            if f in os.listdir(subdir):
                print "remove dir: " + os.path.join(subdir, f)
                deldir(os.path.join(subdir, f))
        elif os.path.isfile(file):
            if f in os.listdir(subdir):
                print "remove file: " + os.path.join(subdir, f)
                os.remove(os.path.join(subdir, f))
        else:
            pass



if __name__ == '__main__':
    print "hello world!"
    remove('/home/huiwu_liu/goldendict', '/home/huiwu_liu')

