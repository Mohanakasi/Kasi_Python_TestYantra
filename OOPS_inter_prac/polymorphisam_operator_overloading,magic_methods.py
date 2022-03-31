"""overloaded"""
"""if all the methods having same name and different data type as an arguments to it"""
"""for operators overloading is possible but in method it is not possible"""
"""method overloading is not possible ecause the data type of the arguments we are pasing implicitly
defined by the pvm we no need to define it if change the type of it it will raised to error\n
this is the reason method overloding is not possible \n
the same also affected to constructor also because that is also inbuilt method 
but we can define the method with same name again with what data tpe we needed this is going to modify the \n
older method with new method and whenever method is calle new method is invoked this is called method overiding"""
class Book(object):
    def __init__(self, pages):
        self.pages = pages

    "python virtual machiene is responsible for calling __add__ inplicitly"
    def __add__(self, other):
        print("__add__ is implicitly calling")
        return self.pages+other.pages

    def __sub__(self, other):
        print("__sub__ is implicitly calling")
        return self.pages - other.pages
    def __mul__(self, other):
        print("__mul__ is implicitly calling")
        return self.pages * other.pages
    # def __iadd__(self, other):
    #     return self += other
    def __str__(self):
        print("__str__ is calling")
        return str(self.pages)

b1 = Book(1008)
b2 = Book(20)
print(type(b1+b2))

"""overloaded"""
"""if all the methods having same name and different data type as an arguments to it"""
