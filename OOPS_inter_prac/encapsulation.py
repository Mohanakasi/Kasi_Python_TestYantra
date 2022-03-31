"encapsulation"
"it is a process of hiding the data or attributes in a single unit"
"""access specifiers"""
"""public access specifiers"""
"""protected access specifiers"""
"""these are created with _ as starting these can access inside the class but as per convention it \n
can not be accessed outside of the class"""

class Login:
    user_name = 'Mohana kasi'
    _password = "kasi.jmr@2020"
    def displaY(self):
        print(Login._password)

print(Login._password)

"""private access specifiers"""
"""these are prefixed with __ these can only accessed inside the class it can not be accessed out side of the 
class """
class Company:
    company_name = "test yantra"
    __project_details = 'alpha'
    def project_info(self):
        print(self.__project_details)

a = Company()
a.project_info()
# Company.__projec ---> attribute also not visible out side of the class

"""property decorator"""
"""it is used to create a property inside the class while creation all the methods should have same names"""
"""by using the property decorator we can give access the user to modify the protected variables  and
if you want to restrict to modify the protected variables and deletig it"""
class Emp:
    company = 'abc'
    __project = 'alpha'
    @property
    def project_data(self):
        print(Emp.__project)

    @property.setter
    def project_data(self, new):
        Emp.__project = new
        print(f"modified project is {Emp.__project}")

e = Emp()
e.project_data
