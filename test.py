#!/usr/bin/python -tt
import sys

class Solution(object):
    def countAndSay(self, n):
        result = []
        result.append(str(1))
        i = 0
        b = 1
        s = ''
        while i < n:
            s = self.say_num(b)
            print repr(s)
            print s
            result.append(s)
            b = int(s)
            i = i+1
        return result
    def say_num(self,n):
        say=''
        y = 1
        ns = str(n)
        if n == 1:
            return '11'
        if n == 11:
            return '21'
        for i in range(len(ns)-1):
            if ns[i] == ns[i+1]:
                y = y + 1
            else:
                x = str(y)+ns[i]
                say += x
                print "the result is" + say
                y = 1
        if ns[len(ns)-1] != ns[len(ns)-2]:
            x = str(1)+ns[len(ns)-1]
            say += x
        return say

a = Solution()
print a.countAndSay(23)
