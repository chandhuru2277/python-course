class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    @staticmethod
    def get_count():
        print("count: ", Example.count)

    @classmethod
    def show_count(self):
        print("Count: ", self.count)


c1 = Example()
c1.show_count()
c2 = Example()
c2.show_count()

Example.get_count()
