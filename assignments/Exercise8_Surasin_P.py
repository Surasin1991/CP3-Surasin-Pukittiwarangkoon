userInput = input("Input Username >>> : ")
passInput = input("Input Password >>> : ")
if userInput == "admin" and passInput == "12345":
    print("Correct")
    print("::--Welcome To Big G Shop--::")
    print("<3--<3--Product List--<3--<3")
    print("1.WaterDrink 10 THB")
    print("2.Banana     20 THB")
    print("3.Chocolate  30 THB")
    print("4.Egg         5 THB")
    p1 = 10
    p2 = 20
    p3 = 30
    p4 = 5
    SelectProduct = input("Select your Product >>> : ")
    Quantity = int(input("How many do you want >>> : "))
    if SelectProduct == "1":
        print("your total price =",p1*Quantity,"THB")
    elif SelectProduct == "2":
        print("your total price =",p2*Quantity,"THB")
    elif SelectProduct == "3":
        print("your total price =",p3*Quantity,"THB")
    elif SelectProduct == "4":
        print("Your total price =",p4*Quantity,"THB")
    else:
        print("Sorry, We don't have the product you need")
else:
    print("Username or Password Incorrect !")
print("<3--<3--Thank you for your shopping--<3--<3")



