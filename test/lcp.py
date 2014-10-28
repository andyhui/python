#!/usr/bin/env python
# encoding: utf-8

import pdb

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs :
            return ""
        lcp_str = strs[0]
        for i in range(0,len(strs)):
            pdb.set_trace()
            if len(strs[i]) == 0 or len(lcp_str) == 0:
                return ""
            lcp_len = len(strs[i]) if len(strs[i]) <= len(lcp_str) else len(lcp_str)
            for j in range(0,lcp_len):
                if not lcp_str[j] == strs[i][j]:
                    break
                else:
                    j = j + 1
            #j = j + 1
            lcp_str = strs[i][:j]
        return lcp_str

a = Solution()
str = a.longestCommonPrefix(["a","b","abc"])
print str
