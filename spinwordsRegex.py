import re
def spin_words(sentence):
    retval=""
    for ind,word in enumerate(re.split("\s",sentence)):
        if len(word) >= 5:
            word=''.join(list(word)[::-1])
        retval+=word+" "
    return retval.strip()
