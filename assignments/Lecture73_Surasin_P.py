systemMenu = {'ข้าวหมกไก่':45,'ข้าวมันไก่':40,'ข้าวมันไก่ผสม':50,'ข้าวหน้าไก่พิเศษ':45}
menuList = []
totalPrice = []
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice.append(menuList[number][1])
while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()
print("Total Price =",sum(totalPrice))