# Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

obj = Calculator(94,10)
data = obj.add()
print(data)
data = obj.subtract()
print(data)
data = obj.multiply()
print(data)
data = obj.divide()
print(data)
