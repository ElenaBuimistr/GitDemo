class Calculator:
    num = 100

    def GetData(self):
        print('I am executing as a method in class')


Calculator()

obj = Calculator() #syntax to create object in Python
obj.GetData()
print(obj.num)