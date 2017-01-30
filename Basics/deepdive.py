class Man:
    var1 = 0
    var2 = 0

    def __init__(self, x, y):
        self.var1 = x
        self.var2 = y

    def add(self):
        return self.var1 + self.var2


obj1 = Man(3, 4)
obj2 = Man(5, 6)

print("obj1.var1=", obj1.var1)
print("obj1.var2=", obj1.var2)

print("obj2.var1=", obj2.var1)
print("obj2.var2=", obj2.var2)

print("Obj1.add=", obj1.add())
print("Obj2.add=", obj2.add())
