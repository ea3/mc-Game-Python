class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1 :
            print("WIII, This is fun")
        elif self.ratio == 1:
            print("This is hard work, but I am flying")
        else:
            print("I think I will just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()



class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swin(self):
        print("Come on it, but it is a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a PENGUIN")


# def test_duck(duck):
#     duck.walk()
#     duck.swin()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # test_duck(donald)
    # percy = Penguin()
    # test_duck(percy)