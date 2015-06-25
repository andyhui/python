#!/usr/bin/python -tt

import sys

def word_count_dictionary(filename):
	wordscount = {}
	f = open(filename,'r')
	for line in f:
		words = line.split()
		for word in words:
			word = word.lower()
			if not word in wordscount:
				wordscount[word] = 1
			else:
				wordscount[word] = wordscount[word] + 1
	f.close()
	return wordscount


def main():
	filename = sys.argv[1]
	words_count = word_count_dictionary(filename)
	words = sorted(words_count.keys())
	for word in words:
		print word,words_count[word]

if __name__ == '__main__':
	main()

