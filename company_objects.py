class Person:
    def __init__(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email

    def getFullName(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def getEmail(self):
        return self.email

class Customer(Person):
    def __init__ (self, fname, lname, email, number):
        Person.__init__(self, fname, lname, email)
        self.cust_number = number

    def getNumcust(self):
        return self.cust_number


class Employee(Person):
    def __init__ (self, fname, lname, email, SSN):
        Person.__init__(self, fname, lname, email)
        self.SSN = SSN

    def getSSN(self):
        return self.SSN
