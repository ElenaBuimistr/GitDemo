# file = open('test.txt')
#
# file.close()   is equal to  with open('test.txt') as file:

with open('test.txt', 'r') as reader:   # open the file and after all manipulations closes it
    content = reader.readlines()  #read the file and store the files in the list
    reversed(content)  # reverse the list
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)  # right it back to the file




