inFile = open("samplecode.txt", "r")
codeLines = inFile.readlines()
variables = []
newLines = []
for line in codeLines:
    line = line.split()
    currLine = ""
    n = 0
    for word in line:
        if word == "var":
            variables.append(line[n+1])
        elif word == variables[0]:
            word = "SCRAMBLED"
        currLine += word + " "
        n += 1
    newLines.append(currLine)

for line in newLines:
    print(line)

