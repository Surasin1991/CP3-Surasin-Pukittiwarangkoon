def vatCalculate(totalPrice):
    totalPrice = float(input("enter your price : "))
    result = totalPrice+(totalPrice*7/100)
    return result

print(("Price Include vat = "),vatCalculate(0))