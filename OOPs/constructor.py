class CAR:
    def __init__(self, price):
        # instance variable
        self.price = price

    def car_price(self):
        return self.price

inovo = CAR(200000)
print("Inovo Car price: ", inovo.car_price())

swift = CAR(500000)
print("Swift Car price:", swift.car_price())


