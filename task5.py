#!/usr/bin/env python
from distsim import *
import argparse
# complete this code
# you will need to run this script twice to predict glove and word2vec respectively


def main():
    # getting input from the command line argument parser for configurations 
    parser = argparse.ArgumentParser()
    parser.add_argument("-emb", default="glove.100d.5K.txt",
                        help="glove emb file")
    parser.add_argument(
        "-analogy", default="word-test.v3.txt", help="analogy file")
    parser.add_argument("-outfile", default="pred.glove.txt",
                        help="w2v output file")
    # collecting data from files and initialising variables
    args = parser.parse_args()
    table = load_table(args.emb)
    c_tot = 0  # total count
    c_suc = 0 # total successfull count in first predictions
    c_suc_5 = 0 # total successfull count in first five predictions
    c_suc_10 = 0 # total successfull count in first ten predictions
    result = ''

    # read file and extract each line
    with open(args.analogy, 'r') as fp:
        lineObj = fp.readlines()
        # iterate on every line
        for i in range(len(lineObj)):
            #  if there is a demaracation of new group
            if(lineObj[i].strip()[0]) == ':':
                # initalisation for the first group
              if(i<5):
                rel_group = lineObj[i].strip()
              # if there are words in this group perform calculations before moving to next group 
              if(c_tot != 0):
                  prev_per = float(c_suc*100/c_tot)
                  prev_per_5 = float(c_suc_5*100/c_tot)
                  prev_per_10 = float(c_suc_10*100/c_tot)
                  result += rel_group.replace(':', '', 1)+': '+str(
                      prev_per/100)+' '+str(prev_per_5/100)+' '+str(prev_per_10/100)+'\n'
            #  reset variables for new group
              c_tot = 0
              c_suc = 0
              c_suc_5 = 0
              c_suc_10 = 0
              rel_group = lineObj[i].strip()

            
            # get words, calulcate their cossim and predict using prewritten fucntions
            elif(lineObj[i].strip().split(" ")[0]) != '//':
                words = lineObj[i].strip().split(" ")
                v1 = get_vector(words[0], table)
                v2 = get_vector(words[1], table)
                v3 = get_vector(words[3], table)
                v4 = v1 - v2 + v3
                # calulate vector and check for nearst matching word. Here n =10 so that we don't have multiple calls to the function.
                exp_word = show_nearest(table, v4, set(
                    [words[0], words[1], words[3]]), n=10)
                c_tot += 1
                # update count on basis of when they were predicted
                for idx, e_w in enumerate(exp_word):
                    if (words[2] == e_w[0]):
                        if(idx == 0):
                            c_suc += 1
                        if(idx < 5):
                            c_suc_5 += 1
                        c_suc_10 += 1               
                # calculations for the last iteration and writing it to file. 
                if(i+1 == len(lineObj)):
                    prev_per = float(c_suc*100/c_tot)
                    prev_per_5 = float(c_suc_5*100/c_tot)
                    prev_per_10 = float(c_suc_10*100/c_tot)
                    result += rel_group.replace(':', '', 1)+': '+str(
                        prev_per/100)+' '+str(prev_per_5/100)+' '+str(prev_per_10/100)+'\n'
                    with open(args.outfile, 'w+') as fp:
                        result.strip()
                        fp.write(result)


if __name__ == '__main__':
    main()
