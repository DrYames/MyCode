import csv


CSV_FILENAME = "monthly_sales.csv"


def write_to_CSV_File(monthlySales):
    with open(CSV_FILENAME, "w", newline = "") as file:
        writer_object = csv.writer(file)
        writer_object.writerows(monthlySales)
    
def read_from_CSV_File():
    try:
        products = []
        with open(CSV_FILENAME, newline = "") as file:
            reader_object = csv.reader(file)
            for row in reader_object:
                products.append(row)
                
        return products
    
    except FileNotFoundError:
        return None
