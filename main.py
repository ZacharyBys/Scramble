import string
import random
def randomString(size=8, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

inFile = open("samplecode.txt", "r")
outFile = open("scrambledcode.txt", "w")

codeLines = inFile.readlines()
variables = []
replacementVariables = []
newLines = []

# Replaces variables with randomly generated strings
################################################################################
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
################################################################################


# Squishes Lines of code together randomly
################################################################################
scrambledLines = []
x=0
while (x < len(newLines)) :
    addedLine = newLines[x]
    while (random.randint(1,2) == 1):
        x += 1
        if (x < len(newLines)):
            addedLine += newLines[x].strip()
    
    x += 1
    scrambledLines.append(addedLine)  
################################################################################

outFile.writelines(scrambledLines)

inFile.close()
outFile.close()




