menuList = []
totalPrice = []
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number])
while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])
        totalPrice.append(menuPrice)
showBill()
print("TotalPrice = ",sum(totalPrice))
