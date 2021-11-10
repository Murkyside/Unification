class Example:
  classVariable = 52

  def __init__(self,myInput):
    self.objectVariable = myInput

  
  def classMethod(self,number):
    print(self.objectVariable + number)

anExample1 = Example(76)
anExample2 = Example(22)

print(anExample1.objectVariable, anExample2.objectVariable)
print(anExample1.classVariable, anExample2.classVariable)

anExample1.classMethod(3)
anExample2.classMethod(4)
#bruh