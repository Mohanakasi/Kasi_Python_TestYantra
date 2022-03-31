class Company:
    company_name = 'Test Yantra'
    Branch = 'kathriguppe'
    def __init__(self, name, age, sal):
        self.name = name
        self.age= age
        self.sal = sal

    def display(self, class_name):
        print(class_name.company_name)
        print(self.name)
        print(self.age)
        print(self.sal)

    @classmethod
    def company_change(cls, new_company, branch):
        cls.company_name = new_company
        cls.Branch = branch

class Branch1(Company):
    pass
e1 = Branch1('kasi',25,30000)
Branch1.company_change("tcs","kolkatta")
e1.display(Branch1)
print(Branch1.company_name)


class Ecomerce:
    items_price = {"laptop": 50000, "watch": 8000}
    items_quantity = {"laptop": 5, "watch": 3}
    discount_perce = 10
    def __init__(self):
        self.cart = {}

    @staticmethod
    def price_caluculator(item):
        cost = Ecomerce.items_price[item]
        discount_price = cost/Ecomerce.discount_perce
        price = cost - discount_price
        return price

    def add_to_cart(self, item, quantity):
        if item in Ecomerce.items_quantity and quantity < Ecomerce.items_quantity[item]:
            self.cart[item] = self.price_caluculator(item)
        else:
            raise "outof stock"
    @classmethod
    def change_discount(cls, percentage):
        cls.discount_perce = percentage

i1 = Ecomerce()
i1.add_to_cart('laptop',2)
print(i1.cart)
i1.change_discount(3)
i2 = Ecomerce()
i2.add_to_cart('laptop',1)
print(i2.cart)
i1.change_discount(35)
i1.add_to_cart("watch", 2)
print(i1.cart)
print(Ecomerce.discount_perce)


"""callable creation"""
class Prime_check:

    def __call__(self, number):
        print("call invoked")
        for i in range(2, number):
            if number % i == 0:
                print(f"{number}not a prime")
                break
        else:
            print(f"{number}prime")

# obj1 = Prime_check()
# obj1(7)
# obj2 = Prime_check()
# obj2(85)
Prime_check() # object creation without storing into a object variable (the same concept used for class decorator)
Prime_check()(12) # obj


"""class decorator"""
class Positive_decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result < 0:
                return abs(result)
            return result
        return wrapper
@Positive_decorator()
def sub_(a,b):
    return a-b
print(sub_(100,500))

"""calling main function n times using class decoratoer"""
class n_time_deco:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                func(*args, **kwargs)
        return wrapper

@n_time_deco(8)
def string_reverse(string_):
    print(string_[::-1])
string_reverse("kasi nadh")

class Greet:
    def __init__(self, msg='good evening'):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.msg)
            func(*args, **kwargs)
        return wrapper
@Greet()
def login_page(user_name, password):
    print(f"enter the user name:{user_name}")
    print(f"enter the password:{password}")
    print(f"Login")
    print("user logged in successfully")
# login_page('kasi','jmr123')






