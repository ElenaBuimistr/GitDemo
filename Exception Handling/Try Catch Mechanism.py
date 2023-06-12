try:  # tryes to run the next code
    with open('text23.txt', 'r') as reader:
        content = reader.readlines()

except:  # if the try fails the info is shown to the user - customized message
    print('There is the problem in the previous block')


try:  # tryes to run the next code
    with open('text23.txt', 'r') as reader:
        content = reader.readlines()

except Exception as e:  # if the try fails the message returned by Python  is shown to the user
    print(e)

finally:
    print('It is all cleaned!')  # To clean all the fake data etc. what was used in all the tests