#Monthly Sales ch07 from CIS3145 by James Porter for 2/21/21
##Rework for Week 5

def display_menu():
    print("COMMAND MENU")
    print("monthly   - View monthly sales")
    print("yearly    - View yearly summary")
    print("edit      - Edit sales for a month")
    print("exit      - Exit Program")
    print()
def command_monthly(monthlySales):
    print("Month \tSales")
    for row in monthlySales:
        print (row[0] + " - \t" + (row[1]))
    print()
def command_yearly(monthlySales):
        total = 0
        months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for months in len(monthlySales(row[0])):
            total = total + int(row[1])
            total = sum(monthlySales)
            print("Yearly total:   ", total)
            average = int(total / len(monthlySales(row[1])))
            print("Monthly average: ", round(average, 2))
            print()
def command_edit(monthlySales):
    months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #new = []
    month = input("Three-letter Month: ")
    if month not in months:
        print("Invalid three-letter month.")
        print()
    else:
        sales = input("Sales Amount: ")                                          
        months_list = months.index(month)
        monthlySales[months_list][1] = sales
        print("Sales amount for " + month + " was modified.")
        print()
def main():
        print("Monthly Sales program")
        print()
        
        monthlySales = [['Jan', '616'],['Feb','466'],['Mar', '796'], ['Apr', '238'], 
			  ['May', '310'], ['Jun', '726'], ['Jul', '987'], ['Aug', '604'], 
			  ['Sep', '951'], ['Oct', '958'], ['Nov', '238'], ['Dec', '610']]
    
        display_menu()
        while True:
            command_input = input ("Command: ")
            if command_input == "monthly":
                command_monthly(monthlySales)
            elif command_input == "yearly":
                command_yearly(monthlySales)
            elif command_input == "edit":
                command_edit(monthlySales)
            elif command_input == "exit":
                break
            else:
                print("Not a valid option. Please try again.\n")
        print("Bye!")            

if __name__ == "__main__":
    main()
