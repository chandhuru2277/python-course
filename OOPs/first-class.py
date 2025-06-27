# class
class CAR:
    # class method
    def accelerate(self, carname):
        message = f"{carname} is Accelerating..."
        print(message)


# object
audi = CAR()
audi.accelerate("Audi A4")

swift = CAR()
swift.accelerate("Swift C3")
