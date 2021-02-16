def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")  
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input("Select menu>> "))
    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Your total price = ",result)
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
if login():
    showMenu()
    userSelected = menuSelect()
    if userSelected == 1:
        totalPrice = int(input("Enter your price : "))
        vatCalculator(totalPrice)
    elif userSelected == 2:
        priceCalculator()
else:
    print("Username or Password was wrong!")
