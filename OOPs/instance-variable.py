class CAR:
    
    def __init__(self, price,carname):
        # instance variable
        self.price = price
        self.carname= carname
    def car_price(self):
        return self.price

    def gear_count(self,level):
        self.gear=level # method instance variable
        print(self.carname," gear count: ", self.gear) # output: Based upon instance


inovo = CAR(200000,"Inovo")
print("Inovo Car price: ", inovo.car_price())
inovo.gear_count(4)

swift = CAR(500000,"Swift")
print("Swift Car price:", swift.car_price())
inovo.gear_count(5)

