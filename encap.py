class computer:
    def __init__(self):
        self.__maxprice = 34000
    def sell(self):
        print("selling price is:" , self.__maxprice)
    def newmaxprice(self,price):
        self.__maxprice = price

c = computer()
c.sell()

c.__maxprice = 50000
c.sell()

c.newmaxprice(50000)
c.sell()