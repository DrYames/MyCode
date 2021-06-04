#Week 3 Chapter 4 Exercise CIS3145 Sales tax Calculator by James Porter completed 2/3/2021
import CalculationsModule as CM

def main():
    subTotal = 0
    print("Sales Tax Calculator")
    print()
    print("ENTER ITEMS (ENTER -99 TO END)")
    resume = "y"
    while resume.lower() == "y":
        item = float(input("Cost of item : "))
        if item == -99:
            tax = CM.salesTax(subTotal)
            total = CM.netTotal(subTotal, tax)
            print("Total:\t", round(subTotal,2))
            print("Sales Tax:", round(tax,2))
            print("Total after tax:", round(total,2))
            print()
            subTotal = subTotal +99
            resume = input("Again? (y/n): ")
        subTotal += item
if __name__ == "__main__":
    main()
