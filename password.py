
def make_password(length, flagUpper, flagLower, flagDigit):
  print ("{}, {},{},{}".format(length,flagUpper,flagLower,flagDigit))
  import random
  password =[]
  if(not flagUpper and not flagLower and not flagDigit):
      print("At least one of the flags has to be set to True")
  elif (not flagUpper and not flagLower and flagDigit) and length>10:
      print("Only flagDigit is True so length should be less than or equal to 10")
  elif (not flagUpper and flagLower and not flagDigit) and length>26:
      print("Only flagLower is True so length should be less than or equal to 26")
  elif (flagUpper and not flagLower and not flagDigit) and length>26:
      print("Only flagUpper is True so length should be less than or equal to 26")
  elif (flagUpper and flagLower and not flagDigit) and length>52:
      print("flagLowe and  flagUpper are True so length should be less than or equal to 52")
  elif (not flagUpper and flagLower and flagDigit) and length>36:
      print("Only flagUpper is True so length should be less than or equal to 26")
  elif (flagUpper and not flagLower and flagDigit) and length>36:
      print("Only flagUpper is True so length should be less than or equal to 26")
  
  else:
     
      choices=[]
      while True:
              print(choices)
              if flagDigit :
                  newchard = chr(random.randint(48,57))
                  if newchard not in choices:
                      choices.append(newchard)
              if flagUpper :
                  newcharu = chr(random.randint(65,90))
                  if newcharu not in choices:
                      choices.append(newcharu)
              if flagLower :
                  newcharl = chr(random.randint(97,122))
                  if newcharl not in choices:
                      choices.append(newcharl)
              if (len(choices) >= length):
                  break
      random.shuffle(choices)
      return  ''.join(elem for elem in choices[0:length])
   
    
