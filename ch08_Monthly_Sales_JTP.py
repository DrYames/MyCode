#Monthly Sales ch08 from CIS3145 by James Porter for 2/28/21
##Rework for Week 6

import ch08FileIO as IO


CSV_FILENAME = "monthly_sales08.csv"

def display_menu():
    IO.read_from_CSV_File()
    print("COMMAND MENU")
    print("monthly   - View monthly sales")
    print("yearly    - View yearly summary")
    print("edit      - Edit sales for a month")
    print("exit      - Exit Program")
    print()
def monthly(monthlySales):
    print("Month \tSales")
    for row in monthlySales:
        print (row[0] + " - \t" + (row[1]))
    print()
def yearly(monthlySales):
        total = 0
        for row in monthlySales:
            try: 
                total = total + int(row[1])
            except ValueError:
                print("Using sales amount of 0 for null.")
        average = int(total / len(monthlySales))
        average = round(average, 3)
        print("Yearly total:   ", total)
        print("Monthly average: ", average)
        print()
def edit(monthlySales):
    months = ['Jan','Feb','Mar','Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    month = input("Three-letter Month: ")
    if month not in months:
        print("Invalid three-letter month.")
        print()
    else:
        sales = input("Sales Amount: ")                                          
        months_list = months.index(month)
        monthlySales[months_list][1] = sales
        print("Sales amount for " + month + " was modified.")
        IO.write_to_CSV_File(monthlySales)
        print()

def main():
        print("Monthly Sales program")
        print()

        monthlySales = [['Jan', '616'],['Feb','466'],['Mar', '796'], ['Apr', '238'], 
			  ['May', '310'], ['Jun', '726'], ['Jul', '987'], ['Aug', '604'], 
			  ['Sep', '951'], ['Oct', '958'], ['Nov', '238'], ['Dec', 'NA']]
        
        display_menu()
        
        while True:
            command_input = input ("Command: ")
            if command_input == "monthly":
                monthly(monthlySales)
            elif command_input == "yearly":
                yearly(monthlySales)
            elif command_input == "edit":
                edit(monthlySales)

            elif command_input == "exit":
                break
            else:
                print("Not a valid option. Please try again.\n")
        print("Bye!")            

if __name__ == "__main__":
    main()
