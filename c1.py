def compressWord(word, K):
    # Write your code here
    idx = 0
    while(idx<len(word)-(K-1)):
        if(word[idx:idx+K]==word[idx]*K):
            word = word[:idx] + word[idx+K:]
            if(idx-K>=0):
                idx = idx-K
            else:
                idx = 0
        else:
            idx+=1

    return word


print(compressWord("aba", 2))