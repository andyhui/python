#!/usr/bin/env python
# encoding: utf-8

import sys
def words_count_dictionary(filename):
    words_count = {}
    f = open(filename,'r')
    for line in f:
        words = line.split()
        for word in words:
            word = word.lower()
            if not word in words_count:
                words_count[word] = 1
            else:
                words_count[word] = words_count[word] + 1
    f.close()
    return words_count

def main():
    #filename = sys.argv[1]
    filename = raw_input("enter the filename:")
    words = words_count_dictionary(filename)
    words_dictionary = sorted(words.keys())
    for word in words_dictionary:
        print word,words[word]

if __name__ == '__main__':
    main()

