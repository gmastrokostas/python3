class class_1:
    class_var = 500
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def summation(self):
        total = self.var1 + self.var2 + self.var3 + self.class_var
        return total
    

class class_2(class_1):
    def __init__(self, var1, var2, var3, var4):
        super().__init__(var1, var2, var3)
        self.var4 = var4
    def summation2(self):
        total_2 = self.var1 + self.var2 + self.var3 + self.var4
        return total_2

x = class_1(30, 30, 30)
print(x.summation())

z = class_2(100, 100, 100, 1000)

print(z.summation2())

