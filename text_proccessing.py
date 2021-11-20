# This is a file processing sample.

# This simple line of code opens the file created and prints it out.
f = open("textfile.txt")
print(f.read())
f.close()

with open("textfile.txt") as secondFile:
    content = secondFile.read()

# print(content)

# This is creating and writting to the file
with open("testing.txt", "w") as myfile:
    myfile.write("Testing\n")

with open("testing.txt", "a+") as myfile:
    myfile.write("Testing2\nTesting3\n")
    myfile.seek(0)
    fileContent = myfile.read()

# print(fileContent)

with open("twoFiles.txt", "a+") as fullTextFile:
    firstFile = open("testing.txt")
    secondFile = open("textfile.txt")
    fullTextFile.write(firstFile.read())
    fullTextFile.write(secondFile.read())
    fullTextFile.seek(0)
    content = fullTextFile.read()

print(content)
