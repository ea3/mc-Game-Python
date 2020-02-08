class Duck(object):

    def walf(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")


def test_duck(duck):
    duck.walf()
    duck.swin()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)