"""multiple inheritence"""
class module1:
    a = 100
    def __init__(self):
        print("in module1")

    def feature1(self):
        print("feature1 is working fine in module1")
    def feature4(self):
        print("feature 4 is working fine in module1")
class module2:
    a = 1000
    def __init__(self):
        print("in module2")
    # def feature4(self):
    #     print("feature 4 is working fine in module2")
    def feature3(self):
        print("feature 3 is working fine in modile2")
class module3:
    # a = 1008
    # def feature4(self):
    #     print("feature 4 is working fine in module3")

    def feture5(self):
        print("feature5 is not working in module3")

class module4(module2, module3, module1):
    def feature4(self):
        print("feture 4 is overided")
        super().feature4()
        print(self)

obj1 = module4()
# print(obj1.a)
# """method resolution porder of module4"""
# print(module4.mro())
print(obj1)
obj1.feature4()
