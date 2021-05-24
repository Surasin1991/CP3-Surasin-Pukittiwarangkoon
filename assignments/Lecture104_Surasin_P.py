class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastName,"'s Cart")

customer1 = Customer()
customer1.name = "Surasin"
customer1.lastName = "Pukittiwarangkoon"
customer1.addCart()

customer2 = Customer()
customer2.name = "Charkon"
customer2.lastName = "K"
customer2.addCart()

customer3 = Customer()
customer3.name = "Sinsuk"
customer3.lastName = "S"
customer3.addCart()

customer4 = Customer()
customer4.name = "Toni"
customer4.lastName = "Boy"
customer4.addCart()