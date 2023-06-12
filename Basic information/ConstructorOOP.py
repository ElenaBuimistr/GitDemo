class Calculator:
    num = 100 # class variables can be called with self or the name of the class

    def __init__(self, a, b): # instant variables
        self.firstNumber = a
        self.secondNumber = b
        print('I am called automatically when the class is created!')

    def GetData(self):
        print('I am executed as a method in class')

    def Summations(self):
        return self.firstNumber + self.secondNumber + self.num  # self is obligatory for calling the instance variables and


obj = Calculator(2, 3) #syntax to create object in Python, there is the possibility to create several objects for one class
obj.GetData()
print(obj.Summations())

obj1 = Calculator(5, 10) #syntax to create object in Python, there is the possibility to create several objects for one class
obj.GetData()
print(obj1.Summations())

