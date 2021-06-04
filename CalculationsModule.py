"""
This is the calculations module for the ch04 Tax Calculator by James Porter
"""
TAX_RATE = 0.06

def salesTax(subTotal):
    """
    Accepts subTotal (item total argument)
    TAX_RATE = (required)
    Returns tax on subTotal
    """
    tax = subTotal * TAX_RATE
    return tax

def netTotal(subTotal, tax):
    """
    Accepts subTotal and tax on subTotal from salesTax()
    Returns total bill
    """
    total = subTotal + tax
    return total

