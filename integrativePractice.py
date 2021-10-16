# Julio de Jesús Ramírez Fernández A0170508
# Ricardo Arturo Camarena Colón A01703831

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
  aux2 = 1
  dictCharacterToStates = {}
  global dictStatesToCharacter
  dictStatesToCharacter = {}
  for x in range(4, len(generalData)): 
 
    #split generalData to get the transitionsStates
    aux =generalData[x].split('=>')
    # split transitionCharacter to get the state and the character 
    transitionCharacter = aux[0].split(',')
    #  split to get the states of the conrvertion of the character
    transitionStates = aux[1].split(',')
    # check if the transitionCharacter haved been used before 
    if ( transitionCharacter[0] != aux2 ):
      dictCharacterToStates.clear()
    # add to the dict dictCharacterToStates the character and the states 
    dictCharacterToStates[transitionCharacter[1]] = transitionStates
    aux2 = transitionCharacter[0]

    # add a empty dict to the state
    dictStatesToCharacter[transitionCharacter[0]] = {}
    # update the empty dict with the dict of the character and the states
    dictStatesToCharacter[transitionCharacter[0]].update(dictCharacterToStates)



# code from https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/ 
def split(word):
    return [char for char in word]

def validateString(string):  
  #reversing the string using list slicing
  res = string[::-1] 

  for x in res:
    # print(dictStatesToCharacter.get(initialState).get(x))
    if ( (dictStatesToCharacter.get(initialState).get(x)) == None):
      print("the string is not accepted because the character " + x  + " in the state " + initialState + " is not a accepted ")
    else:
      print("the character " + x + " in the state " + initialState + " is accepted")
      nextState = dictStatesToCharacter.get(initialState).get(x)
      print("next state to check")
      print(nextState)
    for y in nextState:
      print("state to check")
      print(y)
      # print(dictStatesToCharacter.get(y).get(x))
      if ( (dictStatesToCharacter.get(y).get(x)) == None):
        print( x + " in the state " + y +" is not a accepted ")
      else:
        print( x + " in the state " + y +" is accepted ")



print("Plase introduce the name of the files with '.txt' at the end")
fileName = input()
fileManagment(fileName)
addTransitionStates()
print("Plase introduce the string to validate")
#get the string from the user
stringUser = input()
stringLetters = split(stringUser)
# print(stringLetters)
validateString(stringLetters)
