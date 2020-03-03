def spin_words(sentence):
    retval=""
    listwords= sentence.split(' ')
    print(listwords)
    for ind,word in enumerate(listwords):
        print (word)
        if len(word) >= 5:
            temp=list(word)
            temp.reverse()
            word=''.join(temp)
        if ind==0:  
            retval+=word
        else:
            retval+=' '+word
    return retval
