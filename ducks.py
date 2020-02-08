class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swin(self):
        print("Come on it, but it is a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a PENGUIN")


def test_duck(duck):
    duck.walk()
    duck.swin()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)