def calc(cards):
  '''
  testfirst = [cards[0]]+cards[1:]
  testlast =[cards[-1]]+cards[0:len(cards)-1]
  print(testfirst)
  print(testlast)
  '''
  testfirst= [cards[0]] + cards[1:]
  testlast =[cards[-1]]+cards[0:len(cards)-1]
  temp=[]
  bonus1=cards[0] * 2
  bonus2=cards[-1] * 2
  for ind,num in enumerate(testfirst):
      
      if ind > 0:
          temp.append(max(testfirst[ind],testfirst[-1]))
          del testfirst[testfirst.index(max(testfirst[ind],testfirst[-1]))]
      else:
          temp.append(num)

  testfirst = list(i for i in temp)
  temp.clear()
      
  for ind,num in enumerate(testlast):
      
      if ind > 0:
          temp.append(max(testlast[ind],testlast[-1]))
          del testlast[testlast.index(max(testlast[ind],testlast[-1]))]
      else:
          temp.append(num)

  testlast = list(i for i in temp)
 
  for ind,item in enumerate(testfirst,start=1):
      bonus1 = bonus1 + item * (2 ** ind)
  for ind,item in enumerate(testlast,start=1):
      bonus2 = bonus2 + item * (2 ** ind)

  print(bonus1,bonus2)
      
  print(max(bonus1,bonus2))

  return max(bonus1,bonus2)
