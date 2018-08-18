'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

import re
from nltk.tokenize import word_tokenize

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def word_list(input_text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    input_text = input_text.lower()
    regex = re.compile('[^a-z ]')
    input_text = regex.sub('', input_text)
    list_of_words = input_text.split(' ')
    for _, j in enumerate(list_of_words):

        j = j.strip()
    return list_of_words

def dict_frequency(list_of_words, index, d_ict):
    """ calculating the frequency of the words occurance in the dictionary """
    for each_word in list_of_words:
        if each_word != "":
            if each_word not in d_ict:
                d_ict[each_word] = [0, 0]
            d_ict[each_word][index] += 1
    return d_ict

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    d_ict = {}
    # iterate through all the docs
    for i,j in enumerate(docs):
        
        doc_id = d_ict.keys()
    # keep track of doc_id which is the list index corresponding the document
    
    # hint: use enumerate to obtain the list index in the for loop

    # add or update the words of the doc to the search index

    # return search index

    docs = set(docs.words('english'))
 
    word_tokens = word_tokenize(example_sent)
 
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
    filtered_sentence = []
    for w in word_tokens:
        if w not in docs:
            filtered_sentence.append(w)
 
    return word_sequence

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
