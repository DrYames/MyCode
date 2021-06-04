#ch09 Sales Report by James Porter for CIS3145 for 3/7/21
#This program dynamically displays a report of sales by quarter
import locale as lc

from locale import setlocale

from locale import currency


def main():

    lc.setlocale(lc.LC_ALL, "us")

    sales = [[1540.0, 2010.0, 2450.0, 1845.0],
        [1130.0, 1168.0, 1847.0, 1491.0],
        [1580.0, 2305.0, 2710.0, 1284.0],
        [1105.0, 4102.0, 2391.0, 1576.0]]
    
    print("Sales Report\n")

    print("{:15}{:>15}{:>15}{:>15}{:>15}".format("Region", "Q1", "Q2", "Q3", "Q4"))
    print("{:<15}{:>15}{:>15}{:>15}{:>15}".format(1,lc.currency(1540.0, grouping = True), lc.currency(2010.0, grouping =True), lc.currency(2450.0, grouping =True), lc.currency(1845.0, grouping =True)))
    print("{:<15}{:>15}{:>15}{:>15}{:>15}".format(2,lc.currency(1130.0, grouping = True), lc.currency(1168.0, grouping=True), lc.currency(1847.0, grouping=True), lc.currency(1491.0, grouping =True)))
    print("{:<15}{:>15}{:>15}{:>15}{:>15}".format(3,lc.currency(1580.0, grouping = True), lc.currency(2305.0, grouping=True), lc.currency(2710.0, grouping= True), lc.currency(1284.0, grouping =True)))
    print("{:<15}{:>15}{:>15}{:>15}{:>15}".format(4,lc.currency(1105.0, grouping=True), lc.currency(4102.0, grouping=True),lc.currency(2391.0, grouping=True),lc.currency(1576.0, grouping=True)))
    print()
    
    #calculating region total
    i = 0
    print("Total Sales by region: ")    
    for region in sales:
        i += 1
        total = 0
        for quarter in region:
            total += quarter
        print("Region " + str(i) + ": " + lc.currency(total, grouping=True))
    print()
    
    i = 0
    annual_total = 0
    #calculating quarter total
    
    print("Total Sales by quarter: ")
    for i in range(len(sales[0])):
        total = 0
        total += sales[0][i] + sales[1][i] + sales[2][i] + sales[3][i]
        print("Q" + str(i+1) + ": " + lc.currency(total, grouping=True))
        annual_total += total
        print()
    
    print("Total annual sales, all regions: ", lc.currency(annual_total, grouping=True))

if __name__ == "__main__":
    main()
