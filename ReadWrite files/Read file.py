file = open('test.txt')

# file.read()  # read all the content of the file

# file.read(5) # read only 5 characters  of the file

# file.readline() # read the single line of the file

# print(file.read())

# print(file.readline())

# print(file.readline())

# Print line by line using readline method

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()



# file.readlines() - will retunn all the text in the format of the list []

# print(file.readlines())
for line in file.readlines():
    print(line)

file.close()



