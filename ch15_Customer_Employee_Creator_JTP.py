#Customer/Employee sorter for CIS3145 by James Porter
from company_objects import Person, Customer, Employee

def newPerson(person): 
    if isinstance(person, Customer):
        print("\nCUSTOMER")
        print("Full name: " + person.getFullName())
        print("Email: " + person.getEmail())
        print("Number: " + person.getNumcust())

    elif isinstance(person, Employee):
        print("\nEMPLOYEE")
        print("Full name: " + person.getFullName())
        print("Email: " + person.getEmail())
        print("SSN: " + person.getSSN())

    elif isinstance(person, Person):
        print("Full name: " + person.getFullName())
        print("Email : " + person.getEmail())
        
def main():
    print("Customer/Employee Data Entry")
    print("\n")
    
    loop = True
    while loop:
        custType = input("Customer or employee? (c/e): ")
        print("\nDATA ENTRY")                   # Get data
        Fname = input("First name: ")
        Lname = input("Last name: ")
        Email = input("Email: ")
        if (custType == 'c'):
            custNum = input("Number: ")
            customer =  Customer(Fname,Lname,Email,custNum)
            person = customer
        elif (custType == 'e'):
            ssn = input("SSN: ")
            employee = Employee(Fname,Lname,Email,ssn)
            person = employee
        elif (custType == ''):
            print("\nPERSON")
            person = Person(Fname,Lname,Email)

        newPerson(person)
        
        cont = input("\nContinue? (y/n): ")  # Check if user has more data
        if (cont == 'y'):
            print()
            loop = True
            
        if (cont == 'n'):
            loop = False

    print("\nBye!")
            
if __name__ == "__main__":
    main()
