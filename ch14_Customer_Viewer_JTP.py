#Customer Viewer Program for CIS3145 ch14 by James Porter

from customer_class import Customer

import csv

def main():

    customerList = []
    with open('customers.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            customerList.append(Customer(row[0],row[1],row[2],row[3],row[4],
                                         row[5], row[6], row[7]))
    customerList.pop(0)

    
    print("Customer Viewer")
    print("Enter the customer ID to view the customer address")
    print()

    while True:
        lookup_id = input("Enter customer ID:")
        print()
        flag = 0
        for customer in customerList:
            if customer.cust_id==lookup_id:
                print(customer.getfullAddress())
                print()
                flag = 1
                break
        if (flag== 0):
            print("\n" + "No customer with that id" + "\n")
        choice = input("\n" + "Continue? (y/n): ")
        print()
        if (choice=="n"):
            print("Bye!")
            break                

if __name__ == "__main__":
    main()
