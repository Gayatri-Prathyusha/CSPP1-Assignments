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


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    lower_text = text.lower()
    word_list = lower_text.split(" ")
    for index_iterable in range(len(word_list)):
        word_list[index_iterable] = re.sub("[^a-z]","",word_list[index_iterable])
    return word_list


def remove_stopwords(words_list):
    stop_words = load_stopwords("stopwords.txt")
    temp_wordlist = words_list[:]
    for each_word in temp_wordlist:
        if each_word in stop_words:
            words_list.remove(each_word)
    return words_list


def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    word_dict = {}
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    # clean up doc and tokenize to words list
    # add or update the words of the doc to the search index
    # return search index
    for index_iterable in range(len(docs)):
        string_text = docs[index_iterable]
        docs[index_iterable] = remove_stopwords(word_list(string_text))    
    #print(docs)
    #print(list(enumerate(docs,0)))
    for each_tuple in list(enumerate(docs,0)):
        each_list = each_tuple[1]
        each_value = each_tuple[0]
        for each_word in each_list:
            if each_word not in word_dict:
                word_dict[each_word] = [(each_value, freq_count(each_list, each_word))]
            else:
                if (each_value, freq_count(each_list, each_word)) not in word_dict[each_word]:
                    word_dict[each_word].append((each_value, freq_count(each_list, each_word)))
    return word_dict

def freq_count(doc,word):
    if word in doc:
        freq_count = doc.count(word)
    return freq_count
#print(freq_count(['fool', 'write', 'code', 'computers', 'understand', 'good', 'programmers', 'write', 'code', 'humans', 'understand'], "computers"))
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
    for var_i in range(lines):
        documents.append(input())
        var_i += 1
    #print(documents)
    # call print to display the search index
    print_search_index(build_search_index(documents))
    
if __name__ == '__main__':
    main()
