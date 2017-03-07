'''
Created on Feb 23, 2017

@author: jackwang
'''
import re
import logging
from logging.config import fileConfig

def break_words(stuff):
    """This function uses regular expression to break up sentence into words
    Please note 
    the '\w' expression
       Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
    the + 
       Matches one or more times
    So '\w+' matches any words that contains alphabetical letter and digits.
    """
    words = re.findall('\w+', stuff)
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(- 1)
    print word

def sort_sentence(sentence, removeduplicate=False):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    if removeduplicate == True:
        words = list(set(words))
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence, True)
    print_first_word(words)
    print_last_word(words)
    logger = logging.getLogger(__name__)
    logger.debug('********* I have printed the first and last word in the list!')


if __name__ == "__main__":

    testSentence = """
    When a wish has touched your heart. This thank you card is perfect for that moment.
    """
    fileConfig('logging.ini')
    logger = logging.getLogger('test')
    logger.propagate = False
    words = sort_sentence(testSentence)
    logger.debug('The sorted words are: %s', words)
