# file-output.py
f = open('test1.txt','r')
message = f.read()

# split data
generalData = message.splitlines()       
print(generalData)       
states = generalData[0].split(',')       #['q0', 'q1', 'q2', 'q3']
alphabet  = generalData[1].split(',')    #['a', 'b']
initialState  = generalData[2]           #q0
finalState  = generalData[3].split(',')  #['q3']

for x in range(4, len(generalData)):
  print(generalData[x]) 
#   agregar datos a diccionario 


f.close()