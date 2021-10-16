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
    #split generalData to get the transitionsStates
    aux =generalData[x].split('=>')
    transitionCharacter = aux[0].split(',')
    transitionStates = aux[1].split(',')
    dictCharacterToStates[transitionCharacter[1]] = transitionStates
    dictStatesToCharacter[transitionCharacter[0]] = {}
    dictStatesToCharacter[transitionCharacter[0]].update(dictCharacterToStates)

  print("dictStatesToCharacter")
  print(dictStatesToCharacter)

# code from https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/ 
def split(word):
    return [char for char in word]

def validateString(string):
  print(string)


print("Plase introduce the name of the files with .txt at the end")
fileName = input()
fileManagment(fileName)
addTransitionStates()
print("Plase introduce the string to validate")
stringUser = input()
stringLetters = split(stringUser)
# print(stringLetters)

