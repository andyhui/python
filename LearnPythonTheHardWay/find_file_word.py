#!/usr/bin/env python
# encoding: utf-8

def find_word(search_term,word_list):
    matching_words = []
    for element in word_list:
        if search_term in element:
            matching_words.append(element)
    return matching_words

def file_word_list(filename):
    f = open(filename,'r')
    word_list = []
    for line in f:
        words = line.split()
        for word in words:
            word_list.append(word)
    return word_list

def main():
    filename = raw_input("Enter filename:")
    search_term = raw_input("Enter search_term:")
    my_word_list = file_word_list(filename)
    #print "word list is:",my_word_list
    words_found = find_word(search_term,my_word_list)
    print "I found",words_found

if __name__ == "__main__":
    main()




