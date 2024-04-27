

class rect1:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        
    def calArea(self):
        return self.height * self.width


    def calPrimeter(self):
        return 2*self.height + 2*self.width
    
    
    def showResult(self):
        area = self.calArea()
        primeter = self.calPrimeter()
        print("Area is: " + str(area))
        print("Primeter is: " + str(primeter))
        

    
rec1 = rect1(4, 3)    

print(rec1.height)
print(rec1.width)

print(rec1.calArea())
print(rec1.calPrimeter())

rec1.showResult()

class rect2(rect1):
    def show():
        print("Class inherited")
    

rec2 = rect2(1, 2)

rec2.show()

print(rec2.height)
print(rec2.width)

print(rec2.calArea())
print(rec2.calPrimeter())

rec2.showResult()