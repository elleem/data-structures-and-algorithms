# from data_structures.hashtable import Hashtable
import string


def first_repeated_word(input_string):
    word_count = {}
    words = input_string.lower().split()


    for word in words:
        #remove punctuation marks from the word
        #thanks to TA assistance because translate was new to me, but I did end up trying split as well for readability
        #I left split
        #I learned that translate with create a translation table to remove punctuation characters
        # word = word.translate(str.maketrans('','',string.punctuation))
        word = word.strip(string.punctuation)

        if word in word_count:
            return word
        else:
            word_count[word] = 1
    return None
