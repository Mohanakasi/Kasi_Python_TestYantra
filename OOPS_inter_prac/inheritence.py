"single level inheritence"
class Employee:
    Company_name = "test yantra"
    def __init__(self, name, desig, sal):
        self.name = name
        self.designation = desig
        self.sal = sal

    def greet(self):
        print(f"hai {self.name} welcome to {self.Company_name}")


class Tester(Employee):
    def __init__(self, name, desig, sal,Branch):
        self.branch = Branch
        super().__init__(name, desig, sal)

t1 = Tester('kasi',25,2400,"Katriguppe")
t1.greet()

"""single level inheritence"""
class Ecomerce:
    def __init__(self):
        self.cart = {}

    def add_cart(self, item, quantity):
        self.cart[item] = quantity

    def check_out(self):
        print(self.cart)

class Amazon(Ecomerce):
    inventery = {"moto_mobile": 3000 ,'samsung_mobile':5000, 'iphone':80000}
    def check_out(self):
        super().check_out()
        for item in self.cart:
            print(f"the {item} price is  --> {self.inventery[item]}, total cost {self.inventery[item]*self.cart[item]}")
p1 = Amazon()
p1.add_cart("moto_mobile",20)
p1.add_cart("iphone",15)
p1.check_out()



