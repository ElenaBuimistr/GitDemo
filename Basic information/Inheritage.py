from ConstructorOOP import Calculator

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 7)

    def GetCompleteData(self):
        return self.num2 + self.num + self.Summations()

obj = ChildImpl()
print(obj.GetCompleteData())
