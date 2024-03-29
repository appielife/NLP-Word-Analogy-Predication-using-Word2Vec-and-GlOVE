from __future__ import division
import sys
import json
import math
import os
import numpy as np


def load_table(filename):
    # Returns a dictionary containing a {word: numpy array for a dense word vector} mapping.
    # It loads everything into memory.

    table = {}
    with open(filename, "r") as f_in:
        for line in f_in:
            line_split = line.replace("\n", "").split()
            w = line_split[0]
            vec = np.array([float(x) for x in line_split[1:]])
            table[w] = vec
    return table


def get_vector(w, table):
# directly call the reference w in table array
    return table[w]

    # Returns a numpy array of a word in table
    # w: word token
    # table: lookup table obtained from load_table()

    # pass


def cossim(v1, v2):
    # v1 and v2 are numpy arrays
    # Compute the cosine simlarity between them.
    # Should return a number between -1 and 1

    # calulating numerator by multiplying all elements of v1 with respective elements of v2 and summing them using numpy array operation
    numerator = (np.sum(v1*v2)) 
    # to calculate denominator by using formula given in the assignment
    d1=np.sqrt(np.sum(np.square(v1)))    
    d2 =  np.sqrt(np.sum(np.square(v2)))
    # using numpy to do the operations on arrays
    denominator= d1*d2  
    #returns calculated cossim value   
    return numerator/denominator




def show_nearest(table, v, exclude_w, n=1, sim_metric=cossim):
    # table: lookup table obtained from load_table()
    # v: query word vector (numpy arrays)
    # exclude_w: the words you want to exclude in the responses. It is a set in python.
    # sim_metric: the similarity metric you want to use. It is a python function
    # which takes two word vectors as arguments.
    
    # return: an iterable (e.g. a list) of n tuples of the form (word, score) where the nth tuple indicates the nth most similar word to the input word and the similarity score of that word and the input word after excluding exclude_w
    # if fewer than n words are available the function should return a shorter iterable
    #
    # example:
    # [(cat, 0.827517295965), (university, -0.190753135501)]

# Solution
    #  initialising an array to store indexes, cossim value and word
    wordIndex = []
    distance = np.array([])
    word = []

    # iterate table for each word
    for w in table.keys():
        # exclude words which are given in exclude_w (can take more than one value also)
        if w in exclude_w:
            continue
        # Calculate distance using cossim function
        distance= np.append(distance,(cossim(v,table[w])))
        word.append(w)
    # sort all the words index by distance 
    temp = np.argsort(distance)
    # pick only the last n distance ( choose words with highest cossim)
    temp = temp[::-1][:n]    
    # get word from index
    for i in temp:
        wordIndex.append((word[i],distance[i]))
    return wordIndex      
      

