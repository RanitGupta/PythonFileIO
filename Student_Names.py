s = open('studentnames.txt', 'r')
i = 0
for newLine in s:
    name = newLine.rstrip('\n')
    if name == "":
        continue
    i += 1
    print("Student " + str(i) + ": " + name)
s.close()
print("There were " + str(i) + " students in the file.")