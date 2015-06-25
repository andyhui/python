#!/usr/bin/env python
# encoding: utf-8
import re
class Solution:
    # @return a string
    def count(self,s):
        t=''; count=0; curr='#'
        print "s is :" + s
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                    print "t is the word:" + t
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s

a = Solution()
a.countAndSay(10)

