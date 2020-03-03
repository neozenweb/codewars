import re
def increment_string(strng):
    sortnumber=re.compile('[0-9]*\d')
    splitstrng = sortnumber.findall(strng)
    print(splitstrng)
    if splitstrng:
        number = int(''.join(splitstrng[-1]).strip(' \t\n\r')) + 1
        strng = strng[0:-len(splitstrng[-1])]
        for i in range(len(splitstrng[-1]) - len(str(number))):
         strng += '0'
        strng += str(number)
    else:
        strng += "1"
    
    return strng
