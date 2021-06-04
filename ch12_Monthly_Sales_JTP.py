#Monthly Sales ch12 from CIS3145 by James Porter for 3/21/21
##Rework for Week 9
import salesIO as IO

def display_menu():
    print("COMMAND MENU")
    print("view   - View sales for specified month")
    print("edit   - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit   - Exit Program")
    print()

def view_sales_dictionary(d):
    try:
        months = ['Jan','Feb','Mar','Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        choice = input("Three-letter Month: ")
        if choice not in months:
            print("Invalid three-letter month.")
            print()
        else:
            sales = d[choice]
            print("Sales amount for " + choice + " is: {0:.2f}".format(sales))
            print()
    except Exception as e:
        print(type(e))
        print (e)

def edit_sales_dictionary(d):
    try:
        print()
        n = []

        months = ['Jan','Feb','Mar','Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        choice = input("Three-letter Month: ")
        if choice not in months:
            print("Invalid three-letter month.")
            print()
        else:
            new_sales = int(input("Sales Amount: "))
            d[choice] = new_sales
            print()
            print("The sales amount for " + choice + " is: {0:.2f}".format(new_sales))
            print()
        d = IO.write_to_file(d)
    except Exception as e:
        print(type(e))
        print (e)            

def total_sales_dictionary(d):
    totals = list(d.values())
    yearly = sum(totals)
    avg = yearly/12
    print("Yearly total: " + "\t\t" + "{0:.2f}".format(yearly))
    print("Monthly average: " + "\t" + "{0:.2f}".format(avg))
    print()

def main():
    print("Monthly Sales program")
    print()
    d = IO.read_from_file()
                
    display_menu()


    while True:
        command_input = input ("Command: ")
        if command_input == "view":
            view_sales_dictionary(d)
        elif command_input == "edit":
            edit_sales_dictionary(d)
        elif command_input == "totals":
            total_sales_dictionary(d)
        elif command_input == "exit":
            break
        else:
            print("Not a valid option. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
