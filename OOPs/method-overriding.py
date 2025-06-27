class Father:
    def speaK(self):
        print("Lould")
class Son(Father):
    def speaK(self):
        print("Silent")

s= Son()
s.speaK()