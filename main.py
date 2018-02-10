import string
import random
def randomString(size=8, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

inFile = open("samplecode.txt", "r")
codeLines = inFile.readlines()
variables = []
replacementVariables = []
newLines = []

for line in codeLines:
    currLine = line
    line = line.split()
    n = 0
    for word in line:
        if word == "var":
            variables.append(line[n+1])
            replacementVariables.append(randomString())
        n += 1
    for index, var in enumerate(variables):
        currLine = currLine.replace(var, replacementVariables[index])

      
    newLines.append(currLine)

for line in newLines:
    print(line)



