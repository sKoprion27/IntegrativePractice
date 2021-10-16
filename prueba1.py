def fileManagment (fileName):
  # file-output.py
  f = open(fileName,'r')
  message = f.read()
  # split data
  global generalData
  generalData = message.splitlines()
  # print(generalData)
  global states
  global alphabet
  global initialState
  global finalState
  states = generalData[0].split(',')       #['q0', 'q1', 'q2', 'q3']
  alphabet  = generalData[1].split(',')    #['a', 'b']
  initialState  = generalData[2]           #q0
  finalState  = generalData[3].split(',')  #['q3']
  f.close()


def addTransitionStates():
  dictCharacterToStates = {}
  global dictStatesToCharacter
  dictStatesToCharacter = {}
  for x in range(4, len(generalData)): 
    print("x")
    print(x)
    #split generalData to get the transitionsStates
    aux =generalData[x].split('=>')
    # split transitionCharacter to get the state and the character 
    transitionCharacter = aux[0].split(',')
    #  split to get the states of the conrvertion of the character
    transitionStates = aux[1].split(',')
    # add to the dict dictCharacterToStates the character and the states 
    dictCharacterToStates[transitionCharacter[1]] = transitionStates
    print("dictCharacterToStates")
    print(dictCharacterToStates)
    # add a empty dict to the state
    dictStatesToCharacter[transitionCharacter[0]] = {}
    # update the empty dict with the dict of the character and the states
    dictStatesToCharacter[transitionCharacter[x+1]].update(dictCharacterToStates)

  print("dictStatesToCharacter")
  print(dictStatesToCharacter)

# code from https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/ 
def split(word):
    return [char for char in word]

def validateString(string):  
  #reversing the string using list slicing
  res = string[::-1] 

  for x in res:
    print(x)
    # print(dictStatesToCharacter.get(initialState).get(x))
    if ( (dictStatesToCharacter.get(initialState).get(x)) == None):
      print("the string is not accepted because" + x + "is not a acceptep characer")
    else:
      nextState = dictStatesToCharacter.get(initialState).get(x)
    for y in nextState:
      print("y : x")
      print(y + ":" + x)

      print(dictStatesToCharacter.get(y).get(x))



print("Plase introduce the name of the files with '.txt' at the end")
fileName = input()
fileManagment(fileName)
addTransitionStates()
# print("Plase introduce the string to validate")
# #get the string from the user
# stringUser = input()
# stringLetters = split(stringUser)
# # print(stringLetters)
# validateString(stringLetters)
