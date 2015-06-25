#!/usr/bin/python -tt

import sys

def word_count_dictionary(filename):
    words_count = {}
    f = open(filename)
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
    print 'start count words'
    filename = sys.argv[1]
    wordscount = word_count_dictionary(filename)
    words = sorted(wordscount.keys())
    for word in words:
        print word,wordscount[word]
if __name__ == '__main__':
        main()
