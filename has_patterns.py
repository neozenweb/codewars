import re
def has_subpattern(string):
    if len(string) > 1 and string[0] ==string[1]:
        return True
    elif len(string) <= 1:
        return False
    else:
        for ind in range(2,len(string)):
             print('['+string[0:ind]+']'+'{1,}')
             pattern = re.compile('['+string[0:ind]+']'+'{1,}')
             mat = re.search(pattern,string[ind+1:])
             print(mat)
             if mat:
                  print(mat)
                  return True
    return False  